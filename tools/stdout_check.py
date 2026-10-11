"""Exercise actual CLI output with redirected non-UTF-8 stdout/stderr."""
from pathlib import Path
import json,os,subprocess,sys,tempfile
ROOT=Path(__file__).resolve().parents[1]
def main():
 checks=[]
 with tempfile.TemporaryDirectory() as tmp:
  base=Path(tmp);context=base/'task.json'
  task={'phase':'build','task':'Türkçe çıktı: ı ş ğ','decision_gap':'Çıktıyı koru'}
  context.write_bytes(json.dumps(task,ensure_ascii=False).encode('utf-8'))
  for encoding in ['latin-1','cp1252']:
   env=dict(os.environ,PYTHONIOENCODING=encoding+':strict',PYTHONUTF8='0')
   for tool in ['clients.py','integrate.py']:
    project=base/(encoding+'-'+tool);project.mkdir()
    args=['--clients','claude,cursor,antigravity'] if tool=='clients.py' else ['--agents']
    for action in ['install','install','verify','remove']:
     argv=[sys.executable,'-B',str(ROOT/'tools'/tool),action,'--project',str(project)]
     if action=='install':argv+=['--context',str(context)]+args
     p=subprocess.run(argv,env=env,capture_output=True)
     assert p.returncode==0,(encoding,tool,action,p.stderr.decode(encoding))
     output=p.stdout.decode('ascii');result=json.loads(output)
     assert result['result'] in ['INSTALLED','UNCHANGED','PASS','REMOVED']
     if 'selection' in result:assert result['selection']['task']==task['task']
     checks.append({'encoding':encoding,'tool':tool,'action':action,'result':result['result']})
 return {'result':'PASS','subprocess_checks':checks,'native_windows':'NOT RUN'}
if __name__=='__main__':print(json.dumps(main(),indent=2))
