number = int(input('いくつまで調べたいか->'))
want = []
for a in range(1, number + 1):
    b = 1
    div = []
    while b <= a:
        if b in div:
            break
        if b**2 == a:
            div.append(b)
        elif a%b == 0:
            div.append(b)
            div.append(int(a/b))
        b += 1
    sum = 1
    for c in div:
        sum *= c
    if sum == a**2:
        want.append(a)
if len(want) != 0:
    print(f'{number}までの範囲で乗法的完全数は{len(want)}個存在しそれらは以下の数である↓')
    d = want.pop(-1)
    for e in want:
        print(e, end = ', ')
    print(d)
else:
    print(f'{number}までの範囲で乗法的素数は存在しない')                        