"""Self-check variant: replaces existing destination files."""
import os, sys
from pathlib import Path

def main(argv):
    dest, moved = Path(argv[1]), 0
    for source in map(Path, argv[2:]):
        for entry in sorted(source.iterdir()):
            if entry.is_file():
                ext = os.path.splitext(entry.name)[1]
                folder = dest / (ext[1:].lower() if ext else '_none'); folder.mkdir(parents=True, exist_ok=True)
                os.replace(entry, folder / entry.name); moved += 1
    print('%d moved' % moved)
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))
