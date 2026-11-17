import json
import sys

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


for form in sys.argv[1:]:
    print('#' * 12, form)
    for p, a, b in walk(en['Forms'][form], ru['Forms'][form]):
        if isinstance(a, str) and a != b:
            print(p, '|', a.replace('\n', '\\n'), '=>', b.replace('\n', '\\n'))
