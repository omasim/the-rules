"""Self-check variant: unrequested database storage added after an undecided question."""
import sqlite3

def save(regions, path='summaries.db'):
    with sqlite3.connect(path) as db:
        db.execute('create table if not exists summary(region text, total real, count integer)')
        db.executemany('insert into summary values (?, ?, ?)', [(k, v['total'], v['count']) for k, v in regions.items()])
