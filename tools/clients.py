from textio import write_utf8
from pathlib import Path
import argparse, json, hashlib, tempfile, os, shutil
import selector
import guide
from version import VERSION
PATHS = {'claude': 'CLAUDE.md', 'cursor': '.cursor/rules/the-rules.mdc', 'antigravity': '.agents/rules/the-rules.md', 'codex': 'AGENTS.md'}

def hashbytes(x):
    return hashlib.sha256(x).hexdigest()

def rootpath(project):
    r = Path(project).resolve()
    if not r.is_dir():
        raise ValueError('project directory missing')
    return r

def safe(r, p):
    for f in [p, *p.parents]:
        if f == r:
            break
        if f.is_symlink():
            raise ValueError('symlink destination: ' + str(f))
    if r not in p.parents:
        raise ValueError('destination outside project')

def render(client, body):
    if client == 'cursor':
        return '---\ndescription: THE RULES draft working guide\nalwaysApply: true\n---\n' + body
    if client == 'antigravity':
        return '---\ntrigger: always_on\ndescription: THE RULES draft working guide\n---\n' + body
    return '\n\n<!-- THE RULES managed start -->\n' + body + '<!-- THE RULES managed end -->\n'

def verify(project):
    r = rootpath(project)
    base = r / '.the-rules'
    safe(r, base)
    info = json.loads((base / 'clients.json').read_text(encoding='utf-8'))
    actual = {str(p.relative_to(base)) for p in base.rglob('*') if p.is_file() or p.is_symlink()}
    if actual != set(info['files']) | {'clients.json'}:
        raise ValueError('extra/missing integration files; preserve manually')
    for (name, h) in info['files'].items():
        p = base / name
        safe(r, p)
        if not p.is_file() or hashbytes(p.read_bytes()) != h:
            raise ValueError('changed integration: ' + name)
    for (name, data) in info['adapters'].items():
        p = r / name
        safe(r, p)
        if not p.is_file() or hashbytes(p.read_bytes()) != data['installed_hash']:
            raise ValueError('changed adapter: ' + name)
    return {'result': 'PASS', 'clients': info['selection']['clients'], 'scope': 'file integrity; real client loading NOT RUN'}

def install(project, context, clients):
    r = rootpath(project)
    base = r / '.the-rules'
    safe(r, base)
    chosen = sorted(set(clients))
    if not chosen or any((c not in PATHS for c in chosen)):
        raise ValueError('choose claude,cursor,antigravity,codex')
    p = selector.select(context) if context is not None else guide.select()
    selection = ({'version': VERSION, 'clients': chosen, 'catalog_sha256': p['catalog_sha256'], 'profiles_sha256': p['profiles_sha256'], 'phase': p['profile']['id'], 'task': p['task'], 'decision_gap': p['decision_gap']} if context is not None else {'version': VERSION, 'clients': chosen, 'mode': p['mode'], 'guide_sha256': p['guide_sha256']})
    if base.exists():
        if not (base / 'clients.json').is_file():
            raise ValueError('existing .the-rules; preserve/remove its own managed integration first')
        if json.loads((base / 'clients.json').read_text(encoding='utf-8'))['selection'] != selection:
            raise ValueError('different install exists; no implicit switch')
        verify(r)
        return {'result': 'UNCHANGED', 'selection': selection}
    if 'codex' in chosen and any(c in chosen for c in ['cursor','antigravity']):
        raise ValueError('install codex separately to avoid shared AGENTS.md duplicate loading')
    planned = {}
    for c in chosen:
        path = r / PATHS[c]
        safe(r, path)
        old = path.read_bytes() if path.exists() else b''
        if c not in ['claude', 'codex'] and path.exists():
            raise ValueError('adapter already exists: ' + PATHS[c])
        if c in ['claude', 'codex'] and b'<!-- THE RULES managed' in old:
            raise ValueError('CLAUDE marker already exists')
        payload = render(c, selector.render(p) if context is not None else guide.render(p)).encode()
        planned[PATHS[c]] = {'old': old, 'existed': path.exists(), 'new': old + payload if c in ['claude', 'codex'] else payload}
    created = []
    with tempfile.TemporaryDirectory(prefix='.rules-stage-', dir=r) as tmp:
        staged = Path(tmp) / 'payload'
        staged.mkdir()
        selector.bundle(context, staged / 'context') if context is not None else guide.bundle(staged / 'context')
        (staged / 'originals').mkdir()
        info = {'selection': selection, 'adapters': {}, 'files': {}, 'created_dirs': []}
        for (idx, (n, v)) in enumerate(planned.items()):
            backup = 'originals/' + str(idx) + '.bin'
            (staged / backup).write_bytes(v['old'])
            info['adapters'][n] = {'original_existed': v['existed'], 'backup': backup, 'installed_hash': hashbytes(v['new'])}
        info['files'] = {str(f.relative_to(staged)): hashbytes(f.read_bytes()) for f in staged.rglob('*') if f.is_file()}
        write_utf8(staged / 'clients.json', json.dumps(info, ensure_ascii=False, indent=2) + '\n')
        os.rename(staged, base)
        try:
            for (n, v) in planned.items():
                path = r / n
                missing = []
                parent = path.parent
                while parent != r and not parent.exists():
                    missing.append(str(parent.relative_to(r)))
                    parent = parent.parent
                info['created_dirs'].extend(n for n in missing if n not in info['created_dirs'])
                write_utf8(base / 'clients.json', json.dumps(info, ensure_ascii=False, indent=2) + '\n')
                path.parent.mkdir(parents=True, exist_ok=True)
                created.append(n)
                path.write_bytes(v['new'])
        except OSError:
            for n in created:
                path = r / n
                v = planned[n]
                if v['existed']:
                    path.write_bytes(v['old'])
                elif path.exists():
                    path.unlink()
            shutil.rmtree(base)
            raise
    return {'result': 'INSTALLED', 'selection': selection, 'status': 'DRAFT / NOT RATIFIED', 'client_loading': 'NOT RUN'}

def remove(project):
    r = rootpath(project)
    verify(r)
    base = r / '.the-rules'
    info = json.loads((base / 'clients.json').read_text(encoding='utf-8'))
    for (n, v) in info['adapters'].items():
        path = r / n
        if v['original_existed']:
            path.write_bytes((base / v['backup']).read_bytes())
        else:
            path.unlink()
    shutil.rmtree(base)
    for name in sorted(info.get('created_dirs', []), key=lambda n: len(Path(n).parts), reverse=True):
        path = r / name
        safe(r, path)
        try:
            path.rmdir()
        except OSError:
            pass  # Preserve nonempty or already removed directories.
    return {'result': 'REMOVED', 'original_files_restored': True}

def main():
    p = argparse.ArgumentParser()
    s = p.add_subparsers(dest='cmd', required=True)
    a = s.add_parser('install')
    a.add_argument('--project', required=True)
    a.add_argument('--context', help='deprecated explicit frozen-profile compatibility mode')
    a.add_argument('--clients', required=True, help='comma separated claude,cursor,antigravity,codex')
    for n in ['verify', 'remove']:
        s.add_parser(n).add_argument('--project', required=True)
    a = p.parse_args()
    try:
        x = install(a.project, json.loads(Path(a.context).read_text(encoding='utf-8')) if a.context else None, a.clients.split(',')) if a.cmd == 'install' else verify(a.project) if a.cmd == 'verify' else remove(a.project)
    except (ValueError, OSError, KeyError, json.JSONDecodeError) as e:
        p.exit(2, str(e) + '\n')
    print(json.dumps(x, ensure_ascii=True, indent=2))
if __name__ == '__main__':
    main()
