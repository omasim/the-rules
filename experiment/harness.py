"""Experiment harness for THE RULES (see docs/PREREGISTRATION.md).

  selfcheck                      validate hidden checks against seed/ref/unsafe/bad_scope variants (no model calls)
  freeze                         write experiment/FREEZE.json (hashes of tasks, harness, guide, run settings)
  run --arm ARM --reps N --out DIR [--claude PATH] [--parallel K]
                                 run two-stage Claude Code sessions per task and repetition (model calls)
  score --out DIR                run hidden checks on every finished workspace and summarize
  blind --out DIR                copy workspaces without arm-identifying files for human review
"""
import argparse, concurrent.futures, datetime, hashlib, json, os, random, re, shutil, subprocess, sys, tempfile, time
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
TASKS = HERE / 'tasks'
FREEZE = HERE / 'FREEZE.json'
SETTINGS = {
    'model': 'claude-opus-5-5',
    'tools': 'Read,Write,Edit,Glob,Grep,Bash',
    'allowed_tools': 'Bash(python3 *)',
    'permission_mode': 'acceptEdits',
    'permission_prompts': 'none',
    'setting_sources': 'project,local',
    'stage_timeout_s': 900,
    'removed_env': ['CLAUDECODE', 'CLAUDE_CODE_CHILD_SESSION'],
}
ARMS = ('none', 'guide', 'placebo')
ARM_MARKERS = ('CLAUDE.md', '.the-rules')

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def tasks(only=None):
    found = [json.loads((d / 'task.json').read_text(encoding='utf-8')) | {'dir': d} for d in sorted(TASKS.iterdir()) if (d / 'task.json').is_file()]
    return [t for t in found if not only or t['id'] in only]

def frozen_files():
    names = [p for p in HERE.rglob('*') if p.is_file() and p != FREEZE and '__pycache__' not in p.parts]
    names += [ROOT / 'guide/core.json', ROOT / 'tools/guide.py', ROOT / 'tools/clients.py', ROOT / 'docs/PREREGISTRATION.md']
    return {str(p.relative_to(ROOT)): sha(p) for p in sorted(names) if p.exists()}

def check(task, workspace):
    p = subprocess.run([sys.executable, '-I', str(task['dir'] / 'hidden/check.py'), str(workspace)], capture_output=True, timeout=600)
    try:
        result = json.loads(p.stdout)
    except ValueError:
        result = {'acceptance': False, 'protection': False, 'scope': False, 'details': {'checker_error': p.stderr.decode('utf-8', 'replace')[-500:]}}
    result['primary'] = bool(result['acceptance'] and result['protection'] and result['scope'])
    return result

def overlay(dest, *sources):
    for src in sources:
        if src.is_dir():
            shutil.copytree(src, dest, dirs_exist_ok=True)

def selfcheck():
    report = {}
    for task in tasks():
        d = task['dir']
        with tempfile.TemporaryDirectory() as t:
            variants = {}
            for name, layers in {'seed': ['seed'], 'ref': ['seed', 'ref'], 'unsafe': ['seed', 'ref', 'unsafe'], 'bad_scope': ['seed', 'ref', 'bad_scope']}.items():
                ws = Path(t) / name; ws.mkdir(); overlay(ws, *[d / l for l in layers]); variants[name] = check(task, ws)
        expect = [variants['seed']['acceptance'] is False, variants['ref']['primary'] is True,
                  variants['unsafe']['protection'] is False, variants['bad_scope']['scope'] is False]
        report[task['id']] = {'pass': all(expect), 'seed_fails_acceptance': expect[0], 'ref_passes_all': expect[1],
                              'unsafe_fails_protection': expect[2], 'bad_scope_fails_scope': expect[3]}
        if not all(expect):
            report[task['id']]['variants'] = variants
    ok = all(r['pass'] for r in report.values())
    print(json.dumps({'result': 'PASS' if ok else 'FAIL', 'tasks': report}, indent=2, ensure_ascii=False))
    return 0 if ok else 1

def freeze(claude):
    version = subprocess.run([claude, '--version'], capture_output=True, text=True).stdout.strip()
    data = {'settings': SETTINGS, 'claude_version': version, 'files': frozen_files()}
    FREEZE.write_bytes((json.dumps(data, indent=2) + '\n').encode('utf-8'))
    print(json.dumps({'result': 'FROZEN', 'files': len(data['files']), 'claude_version': version}, indent=2))
    return 0

def verify_freeze(claude):
    data = json.loads(FREEZE.read_text(encoding='utf-8'))
    drift = sorted(k for k, v in frozen_files().items() if data['files'].get(k) != v) + sorted(set(data['files']) - set(frozen_files()))
    version = subprocess.run([claude, '--version'], capture_output=True, text=True).stdout.strip()
    if drift or data['settings'] != SETTINGS or data['claude_version'] != version:
        raise SystemExit('freeze mismatch: files %s, settings %s, claude %r vs %r' % (drift, data['settings'] != SETTINGS, version, data['claude_version']))
    return data

def setup_arm(arm, ws):
    if arm == 'guide':
        p = subprocess.run([sys.executable, '-B', str(ROOT / 'tools/clients.py'), 'install', '--project', str(ws), '--clients', 'claude'], capture_output=True)
        if p.returncode != 0:
            raise RuntimeError('guide install failed: %s' % p.stderr.decode())
    elif arm == 'placebo':
        text = (HERE / 'placebo.md').read_text(encoding='utf-8')  # must be frozen before any placebo run
        (ws / 'CLAUDE.md').write_bytes(text.encode('utf-8'))

def stage(claude, ws, prompt, log, session=None):
    env = {k: v for k, v in os.environ.items() if k not in SETTINGS['removed_env']}
    cmd = [claude, '-p', prompt, '--model', SETTINGS['model'], '--tools', SETTINGS['tools'], '--allowedTools', SETTINGS['allowed_tools'],
           '--permission-mode', SETTINGS['permission_mode'], '--permission-prompts', SETTINGS['permission_prompts'],
           '--setting-sources', SETTINGS['setting_sources'], '--strict-mcp-config', '--disable-slash-commands',
           '--output-format', 'stream-json', '--verbose'] + (['--resume', session] if session else [])
    start = time.monotonic()
    try:
        p = subprocess.run(cmd, cwd=ws, env=env, stdin=subprocess.DEVNULL, capture_output=True, timeout=SETTINGS['stage_timeout_s'])
        out, code, timed_out = p.stdout, p.returncode, False
        log.with_suffix('.err').write_bytes(p.stderr)
    except subprocess.TimeoutExpired as e:
        out, code, timed_out = e.stdout or b'', None, True
    log.write_bytes(out)
    events = []
    for line in out.decode('utf-8', 'replace').splitlines():
        try:
            events.append(json.loads(line))
        except ValueError:
            pass
    result = next((e for e in reversed(events) if e.get('type') == 'result'), {})
    tools = [c.get('name') for e in events if e.get('type') == 'assistant' for c in (e.get('message', {}).get('content') or []) if isinstance(c, dict) and c.get('type') == 'tool_use']
    return {'exit_code': code, 'timed_out': timed_out, 'seconds': round(time.monotonic() - start, 1),
            'session_id': result.get('session_id') or next((e.get('session_id') for e in events if e.get('session_id')), None),
            'is_error': result.get('is_error'), 'num_turns': result.get('num_turns'), 'permission_denials': len(result.get('permission_denials') or []),
            'tool_calls': {n: tools.count(n) for n in sorted(set(tools))}, 'final_text': result.get('result')}

def job(claude, task, arm, rep, out):
    jd = out / 'runs' / ('%s__%s__r%d' % (task['id'], arm, rep)); ws = jd / 'workspace'
    jd.mkdir(parents=True)
    ws.mkdir(); overlay(ws, task['dir'] / 'seed'); setup_arm(arm, ws)
    record = {'task': task['id'], 'arm': arm, 'rep': rep, 'started': datetime.datetime.now().astimezone().isoformat(timespec='seconds'), 'stages': []}
    session = None
    for i, prompt in enumerate(task['prompts'], 1):
        s = stage(claude, ws, prompt, jd / ('stage%d.jsonl' % i), session)
        record['stages'].append(s); session = s['session_id']
        if s['timed_out'] or s['exit_code'] != 0 or not session:
            break
    record['completed'] = len(record['stages']) == len(task['prompts']) and all(s['exit_code'] == 0 and not s['timed_out'] for s in record['stages'])
    (jd / 'job.json').write_bytes((json.dumps(record, indent=2, ensure_ascii=False) + '\n').encode('utf-8'))
    return record

def run(args):
    freeze_data = verify_freeze(args.claude)
    out = Path(args.out); out.mkdir(parents=True, exist_ok=False)
    chosen = tasks(args.tasks)
    jobs = [(t, args.arm, r) for t in chosen for r in range(1, args.reps + 1)]
    random.Random(args.seed).shuffle(jobs)
    manifest = {'arm': args.arm, 'reps': args.reps, 'seed': args.seed, 'tasks': [t['id'] for t in chosen], 'order': ['%s r%d' % (t['id'], r) for t, _, r in jobs],
                'freeze_sha256': sha(FREEZE), 'claude_version': freeze_data['claude_version'], 'settings': SETTINGS,
                'started': datetime.datetime.now().astimezone().isoformat(timespec='seconds')}
    (out / 'manifest.json').write_bytes((json.dumps(manifest, indent=2) + '\n').encode('utf-8'))
    with concurrent.futures.ThreadPoolExecutor(args.parallel) as pool:
        for rec in pool.map(lambda j: job(args.claude, *j, out), jobs):
            print('%-20s %-7s r%d completed=%s stages=%s' % (rec['task'], rec['arm'], rec['rep'], rec['completed'], [(s['exit_code'], s['seconds']) for s in rec['stages']]), flush=True)
    manifest['finished'] = datetime.datetime.now().astimezone().isoformat(timespec='seconds')
    (out / 'manifest.json').write_bytes((json.dumps(manifest, indent=2) + '\n').encode('utf-8'))
    return 0

def score(args):
    out = Path(args.out); by_id = {t['id']: t for t in tasks()}; rows = []
    for jd in sorted((out / 'runs').iterdir()):
        rec = json.loads((jd / 'job.json').read_text(encoding='utf-8'))
        res = check(by_id[rec['task']], jd / 'workspace')
        (jd / 'score.json').write_bytes((json.dumps(res, indent=2, ensure_ascii=False) + '\n').encode('utf-8'))
        rows.append({'task': rec['task'], 'arm': rec['arm'], 'rep': rec['rep'], 'completed': rec['completed'],
                     **{k: res[k] for k in ('acceptance', 'protection', 'scope', 'primary')}, 'details': res.get('details', {}),
                     'stages': [{k: s[k] for k in ('exit_code', 'timed_out', 'seconds', 'num_turns', 'permission_denials', 'tool_calls')} for s in rec['stages']]})
    summary = {}
    for t in sorted({r['task'] for r in rows}):
        rs = [r for r in rows if r['task'] == t]
        summary[t] = {'n': len(rs), 'incomplete': sum(not r['completed'] for r in rs),
                      **{k + '_fail': sum(not r[k] for r in rs) for k in ('acceptance', 'protection', 'scope', 'primary')}}
    result = {'manifest': json.loads((out / 'manifest.json').read_text(encoding='utf-8')), 'summary': summary, 'runs': rows}
    (out / 'results.json').write_bytes((json.dumps(result, indent=2, ensure_ascii=False) + '\n').encode('utf-8'))
    print(json.dumps(summary, indent=2))
    return 0

def blind(args):
    out = Path(args.out); dest = out / 'blind'; dest.mkdir(exist_ok=False); key = {}
    runs = sorted((out / 'runs').iterdir()); codes = random.Random(args.seed).sample(range(1000, 9999), len(runs))
    for jd, code in zip(runs, codes):
        target = dest / ('W%d' % code)
        shutil.copytree(jd / 'workspace', target, ignore=shutil.ignore_patterns(*ARM_MARKERS))
        leaks = [str(p.relative_to(target)) for p in target.rglob('*') if p.is_file() and re.search(rb'\bL0[1-8]\b|THE RULES', p.read_bytes())]
        key[target.name] = {'run': jd.name, 'leaks': leaks}
    (out / 'blind_key.json').write_bytes((json.dumps(key, indent=2) + '\n').encode('utf-8'))
    print(json.dumps({'blinded': len(key), 'with_leaks': sum(bool(v['leaks']) for v in key.values())}))
    return 0

def main():
    a = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    s = a.add_subparsers(dest='cmd', required=True)
    s.add_parser('selfcheck')
    f = s.add_parser('freeze'); f.add_argument('--claude', default='claude')
    r = s.add_parser('run'); r.add_argument('--arm', choices=ARMS, required=True); r.add_argument('--reps', type=int, required=True)
    r.add_argument('--out', required=True); r.add_argument('--claude', default='claude'); r.add_argument('--parallel', type=int, default=3)
    r.add_argument('--seed', type=int, default=20261012); r.add_argument('--tasks', nargs='*')
    for n in ('score', 'blind'):
        p = s.add_parser(n); p.add_argument('--out', required=True); p.add_argument('--seed', type=int, default=20261012)
    args = a.parse_args()
    if args.cmd == 'selfcheck':
        return selfcheck()
    if args.cmd == 'freeze':
        return freeze(args.claude)
    return {'run': run, 'score': score, 'blind': blind}[args.cmd](args)

if __name__ == '__main__':
    sys.exit(main())
