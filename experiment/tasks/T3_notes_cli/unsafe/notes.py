"""Self-check variant: silently resets a corrupt notes.json and ignores unknown numbers."""
import json, sys

def main(argv):
    try:
        notes = json.load(open('notes.json', encoding='utf-8'))
    except (OSError, ValueError):
        notes = []
    if argv[1] == 'add':
        notes.append({'text': argv[2], 'done': False})
    elif argv[1] == 'list':
        for i, n in enumerate(notes, 1):
            print('%d [%s] %s' % (i, 'x' if n['done'] else ' ', n['text']))
    elif argv[1] == 'done' and int(argv[2]) <= len(notes):
        notes[int(argv[2]) - 1]['done'] = True
    json.dump(notes, open('notes.json', 'w', encoding='utf-8'), ensure_ascii=False)
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))
