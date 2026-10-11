from textio import write_utf8
from pathlib import Path
import tempfile, json
import clients

def main():
    checks = []
    c = {'phase': 'build', 'task': 'Yerel CLI', 'decision_gap': 'Hata sınırı'}

    def reject(fn, label):
        try:
            fn()
        except ValueError:
            checks.append(label)
        else:
            raise AssertionError(label)
    for names in [['claude'], ['cursor'], ['antigravity'], ['claude', 'cursor', 'antigravity']]:
        with tempfile.TemporaryDirectory() as t:
            r = Path(t)
            old = b'# User rules\r\nPreserve me.\r\n'
            (r / 'CLAUDE.md').write_bytes(old)
            (r / '.cursor/rules').mkdir(parents=True)
            (r / '.cursor/rules/user.mdc').write_bytes(b'user rule')
            (r / '.agents/rules').mkdir(parents=True)
            (r / '.agents/rules/user.md').write_bytes(b'user rule')
            clients.install(r, c, names)
            clients.verify(r)
            assert clients.install(r, c, names)['result'] == 'UNCHANGED'
            for n in names:
                text = (r / clients.PATHS[n]).read_text(encoding='utf-8')
                assert 'L04' in text and 'L05' in text and ('DRAFT' in text)
                if n == 'cursor':
                    assert text.startswith('---\n') and 'alwaysApply: true' in text
                if n == 'antigravity':
                    assert 'trigger: always_on' in text
            changed = r / clients.PATHS[names[0]]
            original = changed.read_bytes()
            changed.write_bytes(original + b'edited')
            reject(lambda : clients.remove(r), 'edited adapter preserved ' + ','.join(names))
            changed.write_bytes(original)
            clients.remove(r)
            assert (r / 'CLAUDE.md').read_bytes() == old
            assert (r / '.cursor/rules/user.mdc').read_bytes() == b'user rule'
            assert (r / '.agents/rules/user.md').read_bytes() == b'user rule'
            checks.append('install/verify/idempotent/render/restore ' + ','.join(names))
    with tempfile.TemporaryDirectory() as t:
        r = Path(t)
        (r / '.cursor/rules').mkdir(parents=True)
        write_utf8(r / '.cursor/rules/the-rules.mdc', 'mine')
        reject(lambda : clients.install(r, c, ['cursor']), 'existing adapter refused')
        assert not (r / '.the-rules').exists()
        (r / '.cursor/rules/the-rules.mdc').unlink()
        (r / '.cursor').rename(r / 'external')
        (r / '.cursor').symlink_to(r / 'external')
        reject(lambda : clients.install(r, c, ['cursor']), 'symlink parent refused')
    return {'result': 'PASS', 'checks': checks, 'real_clients': 'NOT RUN'}
if __name__ == '__main__':
    print(json.dumps(main(), indent=2))
