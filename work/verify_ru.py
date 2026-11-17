import json
import re

raw = open('ru.lang', 'rb').read()
print('BOM', raw[:3] == b'\xef\xbb\xbf', 'CRLF', raw.count(b'\r\n'),
      'bare LF', raw.count(b'\n') - raw.count(b'\r\n'), 'trailing', repr(raw[-8:]))
print('size', len(raw))

en = json.load(open('en.lang', encoding='utf-8-sig'))
ru = json.load(open('ru.lang', encoding='utf-8-sig'))


def leaves(o, p=''):
    if isinstance(o, dict):
        for k, v in o.items():
            yield from leaves(v, p + '/' + k)
    elif isinstance(o, list):
        for i, v in enumerate(o):
            yield from leaves(v, p + '/' + str(i))
    else:
        yield p, o


le = list(leaves(en))
lr = list(leaves(ru))
print('leaves', len(le), len(lr), 'paths equal', [p for p, _ in le] == [p for p, _ in lr])

issues = []
for (p, a), (q, b) in zip(le, lr):
    if isinstance(a, str) and isinstance(b, str):
        for name, ch in [('%', '%'), ('|', '|'), ('\\n', '\\n'), ('\n', '\n'),
                         ('{', '{'), ('}', '}'), ('&', '&')]:
            if a.count(ch) != b.count(ch):
                issues.append((p, name, a, b))
print('format issues', len(issues))
for x in issues[:10]:
    print(x)

print('language', json.dumps(ru['Language'], ensure_ascii=False))
print('top keys', list(ru))
