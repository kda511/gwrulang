import json

en = json.load(open('en.lang', encoding='utf-8-sig'))
ru = json.load(open('ru.lang.new', encoding='utf-8-sig'))

def walk(en_o, ru_o, p=''):
    if isinstance(en_o, dict):
        for k, v in en_o.items():
            yield from walk(v, ru_o[k], p + '/' + k)
    elif isinstance(en_o, list):
        for i, v in enumerate(en_o):
            yield from walk(v, ru_o[i], p + '/' + str(i))
    else:
        yield p, en_o, ru_o

for p, a, b in walk(en['Forms']['GWMainForm']['ActionList'], ru['Forms']['GWMainForm']['ActionList']):
    if p.endswith('/Caption'):
        print(p[:-8], '|', a, '=>', b)
