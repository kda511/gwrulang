import json

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


for t in ['Кодер', 'кодер', 'Кодировщик', 'кодировщик', 'Декодер', 'декодер', 'кодек', 'Кодек']:
    hits = [(p, v) for p, v in leaves(ru) if t in v]
    print('###', t, len(hits))
    for p, v in hits[:15]:
        print('  ', p, '=', repr(v)[:110])
