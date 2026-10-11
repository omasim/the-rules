"""Deprecated compatibility entry point; new installs use clients.py --clients codex."""
from pathlib import Path
import argparse,json
import clients,legacy_integrate
from version import VERSION
def install(project,context=None,agents=True):
    if not agents:raise ValueError('context-only legacy install retired; use guide reference directly')
    return clients.install(project,context,['codex'])
def verify(project):
    old=Path(project)/'.the-rules/integration.json'
    return legacy_integrate.verify(project) if old.is_file() else clients.verify(project)
def remove(project):
    old=Path(project)/'.the-rules/integration.json'
    return legacy_integrate.remove(project) if old.is_file() else clients.remove(project)
def main():
    p=argparse.ArgumentParser();s=p.add_subparsers(dest='cmd',required=True)
    a=s.add_parser('install');a.add_argument('--project',required=True);a.add_argument('--context');a.add_argument('--agents',action='store_true')
    for n in ['verify','remove']:s.add_parser(n).add_argument('--project',required=True)
    a=p.parse_args()
    try:
        result=install(a.project,json.loads(Path(a.context).read_text(encoding='utf-8')) if a.context else None) if a.cmd=='install' else verify(a.project) if a.cmd=='verify' else remove(a.project)
    except (ValueError,OSError,KeyError,json.JSONDecodeError) as e:p.exit(2,str(e)+'\n')
    print(json.dumps(result,ensure_ascii=True,indent=2))
if __name__=='__main__':main()
