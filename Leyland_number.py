number = int(input('いくつまでの範囲で調べたいか->'))
want = []
for a in range(1, number + 1):
    s = 0
    x = 2
    while x < a:
        y = 2
        while y < a:
            if (x**y) + (y**x) == a:
                want.append(a)
                s = 1
                break
            y += 1
        if s == 1:
            break
        x += 1
if len(want) != 0:
    print(f'{number}までの範囲でレイランド数は{len(want)}個存在しそれらは以下の数である↓')
    b = want.pop(-1)
    for c in want:
        print(c, end = ', ')
    print(b)
else:
    print(f'{number}までの範囲でレイランド数は存在しない')        