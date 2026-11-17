import json
import re

ru = json.load(open('ru.lang.new', encoding='utf-8-sig'))


def leaves(o, p=''):
    if isinstance(o, dict):
        for k, v in o.items():
            yield from leaves(v, p + '/' + k)
    elif isinstance(o, list):
        for i, v in enumerate(o):
            yield from leaves(v, p + '/' + str(i))
    else:
        yield p, o


words = ['the ', ' and ', ' with ', 'Please', 'Cannot', 'file', 'sound', 'select',
         'setting', 'window', 'effect', 'audio', 'channel', 'volume', 'play',
         'record', 'click', 'Edit', 'View', 'Help']
for p, v in leaves(ru):
    if not isinstance(v, str) or not re.search('[А-Яа-я]', v):
        continue
    hits = [w for w in words if w in v]
    if hits:
        print(p, '|', hits, '|', v[:160])
