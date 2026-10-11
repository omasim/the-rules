"""Regression checks for UTF-8/LF I/O and directory ownership; no native Windows claim."""
from pathlib import Path
import io,json,tempfile
from unittest.mock import patch
import clients,integrate

def main():
    real_open=io.open
    def cp1252_open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None):
        if 'b' not in mode:
            encoding=encoding or 'cp1252'
            if newline is None and any(c in mode for c in 'wax'):
                newline='\r\n'
        return real_open(file,mode,buffering,encoding,errors,newline,closefd,opener)
    context={'phase':'build','task':'Türkçe çıktı: ı ş ğ','decision_gap':'Girdi hatasında çıktıyı koru'}
    checks=[]
    with tempfile.TemporaryDirectory() as t, patch('io.open',cp1252_open):
        r=Path(t)
        clients.install(r,context,['claude','cursor','antigravity']);clients.verify(r)
        body=(r/'.the-rules/context/context.md').read_bytes()
        assert b'\r\n' not in body and 'ç'.encode() in body
        checks.append('cp1252 default and CRLF write simulation: UTF-8 LF context')
        clients.remove(r)
        assert not (r/'.cursor').exists() and not (r/'.agents').exists()
        checks.append('remove only newly created empty adapter directories')
        (r/'.cursor/rules').mkdir(parents=True)
        clients.install(r,context,['cursor','antigravity'])
        (r/'.agents/rules/user.md').write_bytes(b'user')
        clients.remove(r)
        assert (r/'.cursor/rules').is_dir() and (r/'.agents/rules/user.md').read_bytes()==b'user'
        checks.append('preserve preexisting directories and newly added user files')
        integrate.install(r,context,True);integrate.verify(r);integrate.remove(r)
        checks.append('Codex install/verify/remove under cp1252 simulation')
        assert clients.VERSION==integrate.VERSION
        checks.append('shared distribution version')
    return {'result':'PASS','checks':checks,'native_windows':'NOT RUN'}
if __name__=='__main__': print(json.dumps(main(),indent=2))
