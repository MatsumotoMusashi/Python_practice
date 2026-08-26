number = int(input('いくつまでの範囲で調べたいですか->'))
want = [1]
for a in range(2, number + 1):
    i = 1
    div = []
    prime = []
    while i <= a:
        if i in div:
            break
        if i**2 == a:
            if len([b for b in range(1, i + 1) if i%b == 0]) == 2:
                prime.append(i)
        if i**2 != a and a%i == 0:
            div.append(int(a/i))
            if len([b for b in range(1, i + 1) if i%b == 0]) == 2:
                prime.append(i)
            if len([b for b in range(1, int(a/i) + 1) if int(a/i)%b == 0]) == 2:
                prime.append(int(a/i))
        i += 1
    s = 0
    for c in prime:
        if a%(c**2) != 0:
            s += 1
    if s == 0:
        want.append(a)
print(f'{number}までの範囲で多冪数は{len(want)}個存在しそれらは以下の数です↓')
d = want.pop(-1)
for e in want:
    print(e, end = ', ')
print(d)                                