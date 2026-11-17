import json

en = json.load(open('en.lang', encoding='utf-8-sig'))
ru = json.load(open('ru.lang.new', encoding='utf-8-sig'))


def walk(a, b, p=''):
    if isinstance(a, dict):
        for k in a:
            yield from walk(a[k], b[k], p + '/' + k)
    elif isinstance(a, list):
        for i, (x, y) in enumerate(zip(a, b)):
            yield from walk(x, y, p + '/' + str(i))
    else:
        yield p, a, b


for p, a, b in walk(en, ru):
    if isinstance(a, str) and any(w in a.lower() for w in ['static', 'stationary', 'steady']):
        print(p, '|', a, '=>', b)
