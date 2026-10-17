"""Self-check variant: opens the output before validating input, so failures truncate it."""
import csv, json, sys

def main(argv):
    with open(argv[2], 'w', encoding='utf-8') as out:
        regions = {}
        try:
            with open(argv[1], encoding='utf-8', newline='') as f:
                for row in csv.DictReader(f):
                    entry = regions.setdefault(row['region'], {'total': 0.0, 'count': 0})
                    entry['total'] += float(row['amount']); entry['count'] += 1
        except (OSError, ValueError) as e:
            print('error: %s' % e, file=sys.stderr); return 1
        for entry in regions.values():
            entry['total'] = round(entry['total'], 2)
        json.dump({'regions': regions}, out, ensure_ascii=False)
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))
