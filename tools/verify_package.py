from pathlib import Path
import json,hashlib
root=Path(__file__).resolve().parents[1]
for name,h in json.loads((root/'MANIFEST.json').read_text()).items():
 p=root/name
 if hashlib.sha256(p.read_bytes()).hexdigest()!=h:raise SystemExit('FAIL: '+name)
print('PASS: packaged file hashes; not external authenticity or AI performance')
