number = int(input('いくつまでの範囲で調べたいですか->'))
want = []
for a in range(1023456789, number + 1):
    if len(set(b for b in str(a))) == 10:
        want.append(a)
if len(want) != 0:
    print(f'{number}までの範囲でパンデジタル数は{len(want)}個存在しそれらは以下の数です↓')
    c = want.pop(-1)
    for d in want:
        print(d, end = ', ')
    print(c)
else:
    print(f'{number}までの範囲でパンデジタル数は存在しません')                