import json, re

def leaves(o, p=''):
    if isinstance(o, dict):
        for k, v in o.items():
            yield from leaves(v, p + '/' + k)
    elif isinstance(o, list):
        for i, v in enumerate(o):
            yield from leaves(v, p + '/' + str(i))
    else:
        yield p, o

ru = json.load(open('ru.lang.new', encoding='utf-8-sig'))
en = json.load(open('en.lang', encoding='utf-8-sig'))
le = list(leaves(en))
lr = list(leaves(ru))
print('leaves', len(le), len(lr), 'paths equal', [p for p, _ in le] == [p for p, _ in lr])

issues = []
for (p, a), (q, b) in zip(le, lr):
    if isinstance(a, str) and isinstance(b, str):
        for name, ch in [('%', '%'), ('|', '|'), ('\\n', '\\n'), ('\n', '\n'), ('{', '{'), ('}', '}'), ('&', '&')]:
            if a.count(ch) != b.count(ch):
                issues.append((p, name, a, b))
print('format issues', len(issues))
for x in issues[:20]:
    print(x)

skip = {
    'GoldWave', 'GoldWave Link', 'GoldWave v', 'GoldWave Lin&k', 'URL', 'URL:', 'https://',
    'https://...', 'CD ID', 'ISRC:', 'LUFS', 'LRA', 'LFE', 'LU', 'Kaiser 7', 'Hann', 'BPM:',
    'Backspace', 'X', 'Y', 'X:', 'Y:', '&X:', '&Y:', 'x', 'y', 'f', 'x =', 'y =', 'f =',
    'n', 't', 'o', 'rock', 'blues', 'classical', 'country', 'data', 'folk', 'jazz', 'misc',
    'newage', 'reggae', 'soundtrack', '%Y-%m-%d, %H:%M:%S', 'YYYY/MM/DD HH:MM:SS',
    '(vox, snd, dat, aud,  ...)', '4x', '8x', '16x', 'ShapeBox', 'ToolBar', 'SpeechToolBar',
    'EffectWrapper', 'DopplerEffectForm', 'ListActionsSelectAll', 'RemoveButton'
}
same = [(p, a) for (p, a), (q, b) in zip(le, lr) if a == b and isinstance(a, str)
        and re.search(r'[A-Za-zА-Яа-я]', a) and a not in skip and not re.fullmatch(r'&[A-Z]', a)]
print('untranslated candidates', len(same))
for p, a in same[:60]:
    print(' ', p, '=', repr(a))

terms = ['Играть', 'играет', 'петл', 'Петл', 'финиш', 'Финиш', 'ключев', 'Ключев',
         'объем', 'Объем', 'нагрузк', 'Нагрузк', 'квартал', 'подач', 'Подач',
         'выпуск', 'Выпуск', 'остаток средств', 'Остаток средств', 'двухместн',
         'Помогите', 'близко', 'Близко']
print('--- glossary check')
for t in terms:
    hits = [(p, v) for p, v in leaves(ru) if t in v]
    if hits:
        print('###', t, len(hits))
        for p, v in hits[:6]:
            print('  ', p, '=', repr(v)[:120])

print('--- Speed occurrences')
hits = [(p, v) for p, v in leaves(ru) if 'Скорост' in v]
print(len(hits))
for p, v in hits[:25]:
    print(' ', p, '=', repr(v)[:110])
