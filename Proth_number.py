number = int(input('いくつまで調べたいか->'))
want = []
for N in range(2, number + 1):
    k = N - 1
    n = 0
    while k%2 == 0:
        k = int(k/2)
        n += 1
    if k < (2**n):
        if 0 < n:
            if 0 < k and k%2 != 0:
                want.append(N)
if len(want) != 0:
    print(f'{number}までの範囲でプロス数は{len(want)}個存在しそれらは以下の数である↓')
    a = want.pop(-1)
    for b in want:
        print(b, end = ', ')
    print(a)
else:
    print(f'{number}までの範囲でプロス数は存在しない')                       