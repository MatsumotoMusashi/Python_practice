number = int(input('いくつまでの範囲で調べたいか->'))
want = [1]
for a in range(2, number + 1):
    b = 2
    div = []
    while b < a:
        if b in div:
            break
        if b**2 == a:
            div.append(b)
        if b**2 != a and a%b == 0:
            div.append(b)
            div.append(int(a/b))
        b += 1
    l = 0
    for c in div:
        n = a
        s = 0
        while n%c == 0:
            n = int(n/c)
            s += 1
        if c**s == a:    
            l += 1
    if 1 <= l:
        want.append(a)
print(f'{number}までの範囲で累乗数は{len(want)}個ありそれらは以下の数です↓')
d = want.pop(-1)
for e in want:
    print(e, end = ', ')
print(d)                    