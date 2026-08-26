number = int(input('いくつまで調べたいか->'))
prime = [2]
want = []
for a in range(3, number + 1):
    can = 0
    for b in prime:
        if a%b == 0:
            can += 1
    if can == 0:
        prime.append(a)
for c in prime:
    if c not in want:
        d = int(str(c)[::-1])
        if d in prime:
                if c != d:
                    want.append(c)
                    want.append(d)
        else:
            if len([e for e in range(1, d + 1) if d%e == 0]) == 2:
                want.append(c)
want.sort()
if len(want) != 0:
    print(f'{number}までの範囲でエマープは{len(want)}個存在しそれらは以下の数である↓')
    f = want.pop(-1)
    for g in want:
        print(g, end = ', ')
    print(f)
else:
    print(f'{number}までの範囲でエマープは存在しない')        