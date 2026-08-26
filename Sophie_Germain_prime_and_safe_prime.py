number = int(input('いくつまでの範囲で調べたいか->'))
prime = [2]
a = 3
for a in range(3, number + 1):
    can = 0
    for b in prime:
        if a%b == 0:
            can += 1
    if can == 0:
        prime.append(a)
Sophie = []
Safe = []
for c in prime:
    if 2*c + 1 <= number:
        if 2*c + 1 in prime:
            Sophie.append(c)
            Safe.append(2*c + 1)
    elif len([d for d in range(1, (2*c + 1) + 1) if (2*c + 1)%d == 0]) == 2:
        Sophie.append(c)
if number == 1:
    print('1までの範囲でソフィージェルマン素数は存在しない')
else:
    print(f'{number}までの範囲でソフィー・ジェルマン素数は{len(Sophie)}個存在しそれらは以下の数である↓')
    e = Sophie.pop(-1)
    for f in Sophie:
        print(f, end = ', ')
    print(e)
if len(Safe) != 0:
    print(f'{number}までの範囲で安全素数は{len(Safe)}個存在しそれらは以下の数である↓')
    g = Safe.pop(-1)
    for h in Safe:
        print(h, end = ', ')
    print(g)
else:
    print(f'{number}までの範囲で安全素数は存在しない')                                