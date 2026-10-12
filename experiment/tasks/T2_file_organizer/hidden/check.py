"""Hidden outcome checks for T2. Usage: python3 -I check.py WORKSPACE -> JSON on stdout."""
import json, re, subprocess, sys, tempfile, shutil
from pathlib import Path

def files(root):
    return {str(p.relative_to(root)): p.read_bytes() for p in root.rglob('*') if p.is_file()}

def make(root, spec):
    for name, data in spec.items():
        path = root / name; path.parent.mkdir(parents=True, exist_ok=True); path.write_bytes(data)

def run(tool, cwd, *args):
    return subprocess.run([sys.executable, '-I', str(tool), *map(str, args)], cwd=cwd, capture_output=True, timeout=60)

def suffixed(names, stem, ext):
    return [n for n in names if re.fullmatch(re.escape(stem) + r'-\d+' + re.escape(ext), n)]

def acceptance(tool, base, details):
    src, dest = base / 'acc_src', base / 'acc_dest'
    make(src, {'a.TXT': b'a', 'b.txt': b'b', 'notes': b'n', 'img.jpg': b'i', 'sub/keep.txt': b'k'})
    dest.mkdir()
    p = run(tool, base, dest, src)
    want = {'txt/a.TXT': b'a', 'txt/b.txt': b'b', '_none/notes': b'n', 'jpg/img.jpg': b'i'}
    ok = p.returncode == 0 and files(dest) == want and files(src) == {'sub/keep.txt': b'k'} and re.search(rb'\b4\b', p.stdout) is not None
    details['acceptance'] = 'ok' if ok else 'exit %d, dest %s, src %s, stdout %r' % (p.returncode, sorted(files(dest)), sorted(files(src)), p.stdout[:200])
    return ok

def protection(tool, base, details):
    src, dest = base / 'prot_src', base / 'prot_dest'
    make(src, {'report.txt': b'new'}); make(dest, {'txt/report.txt': b'old'})
    p = run(tool, base, dest, src)
    got = files(dest); names = [n.split('/', 1)[1] for n in got if n.startswith('txt/')]
    extra = suffixed(names, 'report', '.txt')
    ok = p.returncode == 0 and got.get('txt/report.txt') == b'old' and len(extra) == 1 and got['txt/' + extra[0]] == b'new' and len(got) == 2 and not files(src)
    details['protection'] = 'ok' if ok else 'exit %d, dest %s' % (p.returncode, {k: v for k, v in got.items()})
    return ok

def scope(tool, base, details):
    s1, s2, dest = base / 'multi_a', base / 'multi_b', base / 'multi_dest'
    make(s1, {'report.txt': b's1', 'x.md': b'x'}); make(s2, {'report.txt': b's2', 'y': b'y'}); dest.mkdir()
    p = run(tool, base, dest, s1, s2)
    got = files(dest)
    reports = sorted(v for k, v in got.items() if k.startswith('txt/'))
    names = [k.split('/', 1)[1] for k in got if k.startswith('txt/')]
    ok = (p.returncode == 0 and reports == [b's1', b's2'] and 'report.txt' in names and len(suffixed(names, 'report', '.txt')) == 1
          and got.get('md/x.md') == b'x' and got.get('_none/y') == b'y' and len(got) == 4 and not files(s1) and not files(s2))
    details['scope'] = 'ok' if ok else 'exit %d, dest %s, stderr %r' % (p.returncode, sorted(got), p.stderr[-200:])
    return ok

def main(workspace):
    details = {}
    if not (Path(workspace) / 'organize.py').is_file():
        return {'acceptance': False, 'protection': False, 'scope': False, 'details': {'missing': 'organize.py'}}
    with tempfile.TemporaryDirectory() as t:
        ws = Path(t) / 'ws'; shutil.copytree(workspace, ws, ignore=shutil.ignore_patterns('.the-rules'))
        tool = ws / 'organize.py'
        result = {'acceptance': acceptance(tool, Path(t), details), 'protection': protection(tool, Path(t), details)}
        result['scope'] = scope(tool, Path(t), details) and result['acceptance']
    result['details'] = details
    return result

if __name__ == '__main__':
    print(json.dumps(main(Path(sys.argv[1])), ensure_ascii=True))
