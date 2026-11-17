import json

en = json.load(open('en.lang', encoding='utf-8-sig'))
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


vals = [v for k, v in en['Internal'].items() if k.startswith('sUndo') or k in ('sRedoMenu', 'sUndoMenu')]
for v in sorted(set(vals)):
    print('=' * 5, repr(v))
    for p, a in leaves(en):
        if a == v and not p.startswith('/Internal'):
            print('  ', p)
