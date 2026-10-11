import json,tempfile
from pathlib import Path
import selector

def main():
 cat,index=selector.load();assert len(cat['laws'])==244
 covered=set();sizes=[]
 with tempfile.TemporaryDirectory() as t:
  for pr in index['profiles']:
   c={'phase':pr['id'],'task':'Yerel CSV özeti','decision_gap':'Hata halinde eski çıktıyı koruma'};p=selector.select(c)
   assert p['binding'] is False and p['check']=='NOT RUN' and len(p['laws'])==2
   assert len(p['excluded_from_context'])==242;covered.update(l['id'] for l in p['laws'])
   dest=Path(t)/pr['id'];lock=selector.bundle(c,dest)
   assert all(selector.sha(dest/n)==h for n,h in lock['files'].items())
   try:selector.bundle(c,dest)
   except ValueError:pass
   else:raise AssertionError('overwrite allowed')
   sizes.append({'profile':pr['id'],'law_count':2,'utf8_bytes':len((dest/'context.md').read_bytes()),'tokens':'NOT MEASURED'})
  for c in [{},{'phase':'unknown','task':'x','decision_gap':'x'},{'phase':'build','task':'','decision_gap':'x'},{'phase':'build','task':'x','decision_gap':None}]:
   try:selector.select(c)
   except ValueError:pass
   else:raise AssertionError('invalid input accepted')
 assert covered=={'L%02d'%i for i in range(1,9)}
 return {'result':'PASS','scope':'selection, source integrity, lock hashes, no overwrite, explicit context validation; no AI effectiveness test','catalog_records':244,'all_core_laws_covered':True,'profiles':sizes}
if __name__=='__main__':print(json.dumps(main(),ensure_ascii=False,indent=2))
