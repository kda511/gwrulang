import json, os

for bi in range(1, 43):
    p = f'work/translations/batch_{bi:03d}.json'
    t = json.load(open(p, encoding='utf-8'))
    q = [v for v in t.values() if '?' in v]
    if q:
        print('batch', bi, 'strings with ?:', len(q))
        for v in q[:12]:
            print('   ', repr(v))
