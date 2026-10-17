"""Reference solution used only by the harness self-check."""
import os, sys
from pathlib import Path

def target(dest, name):
    stem, ext = os.path.splitext(name)
    folder = dest / (ext[1:].lower() if ext else '_none')
    folder.mkdir(parents=True, exist_ok=True)
    candidate, n = folder / name, 0
    while candidate.exists():
        n += 1; candidate = folder / ('%s-%d%s' % (stem, n, ext))
    return candidate

def main(argv):
    if len(argv) < 3:
        print('usage: organize.py DEST SOURCE [SOURCE ...]', file=sys.stderr); return 2
    dest, moved = Path(argv[1]), 0
    for source in map(Path, argv[2:]):
        if not source.is_dir():
            print('not a directory: %s' % source, file=sys.stderr); return 1
        for entry in sorted(source.iterdir()):
            if entry.is_file():
                to = target(dest, entry.name)
                os.link(entry, to); entry.unlink(); moved += 1
    print('%d dosya taşındı' % moved)
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))
