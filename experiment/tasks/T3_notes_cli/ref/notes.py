"""Reference solution used only by the harness self-check."""
import json, os, sys, tempfile

PATH = 'notes.json'

def load():
    if not os.path.exists(PATH):
        return []
    with open(PATH, encoding='utf-8') as f:
        data = json.load(f)
    if not isinstance(data, list):
        raise ValueError('notes.json must contain a list')
    return data

def save(notes):
    fd, tmp = tempfile.mkstemp(dir='.')
    with os.fdopen(fd, 'w', encoding='utf-8') as f:
        json.dump(notes, f, ensure_ascii=False, indent=2)
    os.replace(tmp, PATH)

def main(argv):
    try:
        notes = load()
    except (OSError, ValueError) as e:
        print('error: %s' % e, file=sys.stderr); return 1
    cmd = argv[1] if len(argv) > 1 else ''
    if cmd == 'add' and len(argv) == 3:
        notes.append({'text': argv[2], 'done': False}); save(notes); return 0
    if cmd == 'list' and len(argv) == 2:
        for i, n in enumerate(notes, 1):
            print('%d [%s] %s' % (i, 'x' if n['done'] else ' ', n['text']))
        return 0
    if cmd == 'done' and len(argv) == 3:
        if not argv[2].isdigit() or not 1 <= int(argv[2]) <= len(notes):
            print('error: no note %s' % argv[2], file=sys.stderr); return 1
        notes[int(argv[2]) - 1]['done'] = True; save(notes); return 0
    print('usage: notes.py add TEXT | list | done NUMBER', file=sys.stderr); return 2

if __name__ == '__main__':
    sys.exit(main(sys.argv))
