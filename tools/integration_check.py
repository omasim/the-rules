from pathlib import Path
import tempfile,json
import integrate

def main():
 c={'phase':'build','task':'Yerel CLI','decision_gap':'Hatalı girdide çıktı koruması'};checks=[]
 def reject(fn,name):
  try:fn()
  except ValueError:checks.append(name)
  else:raise AssertionError(name)
 with tempfile.TemporaryDirectory() as t:
  root=Path(t);original=b'# Existing instructions\r\nKeep local conventions.\r\n';(root/'AGENTS.md').write_bytes(original)
  integrate.install(root,c,True);checks.append('install with existing AGENTS')
  assert (root/'AGENTS.md').read_bytes().startswith(original);checks.append('original bytes preserved')
  before=(root/'AGENTS.md').read_bytes();assert integrate.install(root,c,True)['result']=='UNCHANGED';assert (root/'AGENTS.md').read_bytes()==before;checks.append('idempotent')
  reject(lambda:integrate.install(root,dict(c,phase='deliver'),True),'refuse implicit profile replacement')
  integrate.verify(root);checks.append('installed integrity')
  (root/'AGENTS.md').write_bytes(before+b'new user change');reject(lambda:integrate.remove(root),'preserve edited AGENTS')
  (root/'AGENTS.md').write_bytes(before);integrate.remove(root);assert (root/'AGENTS.md').read_bytes()==original;checks.append('exact original restore')
  (root/'AGENTS.md').unlink();integrate.install(root,c,True);integrate.remove(root);assert not (root/'AGENTS.md').exists();checks.append('remove created AGENTS')
  integrate.install(root,c,False);assert not (root/'AGENTS.md').exists();checks.append('context only opt-in')
  f=root/'.the-rules/context/context.md';old=f.read_bytes();f.write_bytes(b'edited');reject(lambda:integrate.verify(root),'detect context mutation');reject(lambda:integrate.remove(root),'preserve edited context');f.write_bytes(old);integrate.remove(root)
  (root/'.the-rules').mkdir();reject(lambda:integrate.install(root,c),'preserve unmanaged directory');(root/'.the-rules').rmdir()
  external=root/'external';external.mkdir();(root/'.the-rules').symlink_to(external);reject(lambda:integrate.install(root,c),'reject destination symlink')
 return {'result':'PASS','checks':checks,'real_AI_loading':'NOT RUN','GitHub_download':'NOT RUN'}
if __name__=='__main__':print(json.dumps(main(),indent=2))
