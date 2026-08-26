number = int(input('いくつまでの範囲で調べたいですか->'))
want = []
for a in range(1, number + 1):
    b = [c for c in range(1, a + 1)]
    s = 0
    for d in b:
        if d**2 < a:
            for e in b:
                if d < e and e**2 < a:
                    if d**2 + e**2 == a:
                        s += 1
    if 1 <= s:
        want.append(a)
if len(want) != 0:
    print(f'{number}までの範囲で異なる二つの平方数であらわせる数は{len(want)}個ありそれらは以下の数です↓')
    f = want.pop(-1)
    for g in want:
        print(g, end = ', ')
    print(f)                                
else:
    print(f'{number}までの範囲で異なる二つの平方数であらわせる数は存在しません')    