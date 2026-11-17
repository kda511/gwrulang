import json, re

en = json.load(open('en.lang', encoding='utf-8-sig'))
ru = json.load(open('ru.lang.new', encoding='utf-8-sig'))


def walk(a, b, p=''):
    issues = []
    if type(a) is not type(b):
        return [(p, 'type', type(a).__name__, type(b).__name__)]
    if isinstance(a, dict):
        if list(a) != list(b):
            issues.append((p, 'keys', list(a), list(b)))
        for k in a:
            if k in b:
                issues += walk(a[k], b[k], p + '/' + k)
    elif isinstance(a, list):
        if len(a) != len(b):
            issues.append((p, 'len', len(a), len(b)))
        for i, (x, y) in enumerate(zip(a, b)):
            issues += walk(x, y, p + '/' + str(i))
    else:
        if isinstance(a, str):
            for name, ch in [('%', '%'), ('|', '|'), ('\\n', '\\n'), ('\n', '\n'),
                             ('{', '{'), ('}', '}'), ('&', '&')]:
                if a.count(ch) != b.count(ch):
                    issues.append((p, name, a, b))
            pa = re.findall(r'%[^%]*%', a)
            pb = re.findall(r'%[^%]*%', b)
            if pa != pb:
                issues.append((p, 'placeholders', pa, pb))
            markers_a = [c for c in a if c in '{}|\n&']
            markers_b = [c for c in b if c in '{}|\n&']
            # '&' accelerates can move; compare only structural markers
            ma = [c for c in a if c in '{}|\n']
            mb = [c for c in b if c in '{}|\n']
            if ma != mb:
                issues.append((p, 'markers order', ma, mb))
            if a and not b:
                issues.append((p, 'empty translation', a))
            if (a[:1].isspace()) != (b[:1].isspace()) or (a[-1:].isspace()) != (b[-1:].isspace()):
                issues.append((p, 'edge space', a, b))
        elif a != b:
            issues.append((p, 'non-string changed', a, b))
    return issues


issues = walk(en, ru)
print('total issues', len(issues))
for x in issues[:40]:
    print(x)
