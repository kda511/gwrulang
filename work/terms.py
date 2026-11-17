import json, re
from collections import Counter

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

vals = [v for p, v in leaves(ru) if isinstance(v, str)]

checks = {
    'реперн': 'реперн',
    'метк': 'метк',
    'Cue ': 'Cue ',
    'Выбор': 'Выбор',
    'выбор': 'выбор',
    'Управление': 'Управление',
    'управлен': 'управлен',
    'Громкость': 'Громкость',
    'громкост': 'громкост',
    'Баланс': 'Баланс',
    'баланс': 'баланс',
    'Высота тона': 'Высота тона',
    'высот': 'высот',
    'Восстановление': 'Восстановление',
    'восстановлен': 'восстановлен',
    'Шумовой затвор': 'Шумовой затвор',
    'шумов': 'шумов',
    'Наложение голоса': 'Наложение голоса',
    'наложен': 'наложен',
    'частот': 'частот',
    'Частот': 'Частот',
    'скорост': 'скорост',
    'Скорост': 'Скорост',
    'запис': 'запис',
    'Запис': 'Запис',
    'воспроизв': 'воспроизв',
    'Воспроизв': 'Воспроизв',
}

for name, sub in checks.items():
    n = sum(1 for v in vals if sub in v)
    print(f'{name!r}: {n}')
