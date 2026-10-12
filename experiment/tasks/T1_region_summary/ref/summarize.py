"""Reference solution used only by the harness self-check."""
import csv, json, os, sys, tempfile

def main(argv):
    if len(argv) != 3:
        print('usage: summarize.py INPUT.csv OUTPUT.json', file=sys.stderr); return 2
    src, dest = argv[1], argv[2]
    regions = {}
    try:
        with open(src, encoding='utf-8', newline='') as f:
            for row in csv.DictReader(f):
                amount = float(row['amount'])
                entry = regions.setdefault(row['region'], {'total': 0.0, 'count': 0})
                entry['total'] += amount; entry['count'] += 1
    except (OSError, KeyError, ValueError) as e:
        print('error: %s' % e, file=sys.stderr); return 1
    for entry in regions.values():
        entry['total'] = round(entry['total'], 2)
    fd, tmp = tempfile.mkstemp(dir=os.path.dirname(os.path.abspath(dest)))
    with os.fdopen(fd, 'w', encoding='utf-8') as f:
        json.dump({'regions': regions}, f, ensure_ascii=False, indent=2)
    os.replace(tmp, dest)
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))
