from pathlib import Path
import tempfile,json,subprocess,sys,hashlib
import clients,guide,integrate,legacy_integrate

def main():
    p=guide.select();assert len(p['laws'])==8
    assert {l['id'] for l in p['laws']}=={'L%02d'%n for n in range(1,9)}
    assert all(l['trigger'] and l['proportionality'] and l['source_ids'] for l in p['laws'])
    body=guide.render(p);checks=[]
    original=json.loads((guide.ROOT/'library/catalog.json').read_text(encoding='utf-8'))
    lookup={law['id']:law for law in original['laws']}
    for law in p['laws']:
        for key in ['id','title','rule','check','proportionality','decision_question','scope','source_ids','status','owner_ratification']:
            assert law[key]==lookup[law['id']][key]
        assert law['level']=='advisory' and law['binding'] is False
        assert law['source_file']=='provenance.json'
    checks.append('original eight law text/source/status preserved')
    with tempfile.TemporaryDirectory() as t:
        root=Path(t)
        for name in ['claude','cursor','antigravity','codex']:
            project=root/name;project.mkdir();path=project/clients.PATHS[name]
            if name in ['claude','codex']:path.write_bytes(b'original\r\n')
            first=clients.install(project,None,[name]);assert 'phase' not in first['selection'] and 'task' not in first['selection'] and 'decision_gap' not in first['selection']
            payload=project/'.the-rules/context'
            selection=json.loads((payload/'selection.json').read_text(encoding='utf-8'))
            prov=json.loads((payload/'provenance.json').read_text(encoding='utf-8'))
            source_ids={x['source_id'] for x in prov['records']}
            for law in selection['laws']:
                assert law['level']=='advisory' and law['binding'] is False
                assert (payload/law['source_file']).is_file()
                assert set(law['source_ids'])<=source_ids
            lock=json.loads((payload/'rules.lock.json').read_text(encoding='utf-8'))
            assert lock['files']['provenance.json']==hashlib.sha256((payload/'provenance.json').read_bytes()).hexdigest()
            before=path.read_bytes();assert all(('L%02d'%n).encode() in before for n in range(1,9))
            assert clients.install(project,None,[name])['result']=='UNCHANGED'
            clients.verify(project)
            source=payload/'provenance.json';old_bytes=source.read_bytes();source.write_bytes(b'changed')
            try:clients.verify(project)
            except ValueError:pass
            else:raise AssertionError('changed source trace accepted')
            source.write_bytes(old_bytes);clients.remove(project)
            if name in ['claude','codex']:assert path.read_bytes()==b'original\r\n'
            else:assert not path.exists()
            checks.append(name+' adaptive core install/repeat/restore')
        old=root/'old';old.mkdir();legacy_integrate.install(old,{'phase':'build','task':'old','decision_gap':'old'},True)
        integrate.verify(old);integrate.remove(old);assert not (old/'AGENTS.md').exists();checks.append('legacy Codex verify/remove compatibility')
        both=root/'both';both.mkdir()
        try:clients.install(both,None,['codex','cursor'])
        except ValueError:pass
        else:raise AssertionError('duplicate discovery allowed')
        assert not (both/'.the-rules').exists();checks.append('shared AGENTS duplicate prevention')
    return {'result':'PASS','checks':checks,'guide_utf8_bytes':len(body.encode()),'tokens':'NOT MEASURED','new_client_loading':'NOT RUN','benefit':'NOT DEMONSTRATED'}
if __name__=='__main__':print(json.dumps(main(),indent=2))
