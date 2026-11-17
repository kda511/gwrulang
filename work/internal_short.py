import json

en = json.load(open('en.lang', encoding='utf-8-sig'))
ru = json.load(open('ru.lang.new', encoding='utf-8-sig'))

rows = []
for k, a in en['Internal'].items():
    b = ru['Internal'][k]
    if isinstance(a, str):
        rows.append((k, a, b))

rows.sort()
for k, a, b in rows:
    if len(a) <= 75:
        print(k, '|', a.replace('\n', '\\n'), '=>', b.replace('\n', '\\n'))
