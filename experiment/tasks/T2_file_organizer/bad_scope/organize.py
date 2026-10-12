"""Self-check variant: stage-1 behaviour only; the authorized multi-source change is missing."""
import os, sys
from pathlib import Path

def main(argv):
    if len(argv) != 3:
        print('usage: organize.py DEST SOURCE', file=sys.stderr); return 2
    dest, source, moved = Path(argv[1]), Path(argv[2]), 0
    for entry in sorted(source.iterdir()):
        if entry.is_file():
            stem, ext = os.path.splitext(entry.name)
            folder = dest / (ext[1:].lower() if ext else '_none'); folder.mkdir(parents=True, exist_ok=True)
            candidate, n = folder / entry.name, 0
            while candidate.exists():
                n += 1; candidate = folder / ('%s-%d%s' % (stem, n, ext))
            os.link(entry, candidate); entry.unlink(); moved += 1
    print('%d moved' % moved)
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))
