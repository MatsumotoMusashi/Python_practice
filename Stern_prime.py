number = int(input('いくつまで調べたいか->'))
if number != 1:
    prime = [2]
    want = [2]
for a in range(3, number + 1):
    can = 0
    for b in prime:
        if a%b == 0:
            can += 1
    if can == 0:
        yes = 0
        for c in prime:
            d = a - c
            if d%2 == 0:
                e = int(d/2)
                f = 1
                while f**2 <= e:
                    if f**2 == e:
                        yes += 1
                    f += 1
        if yes == 0:
            want.append(a)                 
        prime.append(a)
if number == 1:
    print('1までの範囲でスターン素数は存在しない')
else:
    print(f'{number}までの範囲でスターン素数は{len(want)}個存在しそれらは以下の数である↓')
    g = want.pop(-1)
    for h in want:
        print(h, end = ', ')
    print(g)        