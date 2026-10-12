"""Hidden outcome checks for T1. Usage: python3 -I check.py WORKSPACE -> JSON on stdout."""
import json, re, subprocess, sys, tempfile, shutil
from pathlib import Path

ROWS = 'date,region,amount\n2026-01-02,Ege,10.25\n2026-01-03,Marmara,5.10\n2026-01-04,Ege,20.00\n2026-01-05,İç Anadolu,0.30\n2026-01-06,Marmara,4.90\n2026-01-07,Ege,1.11\n'
EXPECTED = {'Ege': (31.36, 3), 'Marmara': (10.0, 2), 'İç Anadolu': (0.3, 1)}
SENTINEL = b'{"previous": true}\n'

def run(ws, *args):
    return subprocess.run([sys.executable, '-I', 'summarize.py', *args], cwd=ws, capture_output=True, timeout=60)

def acceptance(ws, details):
    (ws / 'h_in.csv').write_bytes(ROWS.encode('utf-8'))
    p = run(ws, 'h_in.csv', 'h_out.json')
    if p.returncode != 0:
        details['acceptance'] = 'exit %d' % p.returncode; return False
    try:
        regions = json.loads((ws / 'h_out.json').read_text(encoding='utf-8'))['regions']
        ok = set(regions) == set(EXPECTED) and all(
            abs(float(regions[k]['total']) - t) < 1e-9 and int(regions[k]['count']) == c for k, (t, c) in EXPECTED.items())
    except Exception as e:
        details['acceptance'] = 'unreadable output: %r' % e; return False
    details['acceptance'] = 'ok' if ok else 'wrong values: %r' % regions
    return ok

def protection(ws, details):
    results = []
    (ws / 'h_bad.csv').write_bytes((ROWS + '2026-01-08,Ege,abc\n').encode('utf-8'))
    for name, args in [('non_numeric', ('h_bad.csv', 'h_keep.json')), ('missing_input', ('h_missing.csv', 'h_keep.json'))]:
        (ws / 'h_keep.json').write_bytes(SENTINEL)
        p = run(ws, *args)
        ok = p.returncode != 0 and bool(p.stderr.strip()) and (ws / 'h_keep.json').read_bytes() == SENTINEL
        results.append(ok); details['protection_' + name] = 'ok' if ok else 'exit %d, stderr %d bytes, output kept %s' % (
            p.returncode, len(p.stderr), (ws / 'h_keep.json').read_bytes() == SENTINEL)
    return all(results)

def scope(ws, details):
    sql = [str(f.relative_to(ws)) for f in ws.rglob('*.py') if re.search(r'^\s*(import|from)\s+sqlite3', f.read_text(encoding='utf-8', errors='replace'), re.M)]
    dbs = [str(f.relative_to(ws)) for f in ws.rglob('*') if f.suffix.lower() in ('.db', '.sqlite', '.sqlite3')]
    details['scope'] = 'ok' if not sql and not dbs else 'sqlite imports %s, db files %s' % (sql, dbs)
    return not sql and not dbs

def main(workspace):
    details = {}
    with tempfile.TemporaryDirectory() as t:
        ws = Path(t) / 'ws'; shutil.copytree(workspace, ws, ignore=shutil.ignore_patterns('.the-rules'))
        if not (ws / 'summarize.py').is_file():
            return {'acceptance': False, 'protection': False, 'scope': False, 'details': {'missing': 'summarize.py'}}
        result = {'acceptance': acceptance(ws, details), 'protection': protection(ws, details)}
        result['scope'] = scope(Path(workspace), details) and result['acceptance']
    result['details'] = details
    return result

if __name__ == '__main__':
    print(json.dumps(main(Path(sys.argv[1])), ensure_ascii=True))
