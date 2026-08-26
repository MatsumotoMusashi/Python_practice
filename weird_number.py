from itertools import combinations
number_1 = int(input('調査範囲の初期値(1以上)->'))
number_2 = int(input('調査範囲の最終値->'))
want = []
for a in range(number_1, number_2 + 1):
    b = 2
    s = 0
    div = [1]
    while b < a:
        if b in div:
            break
        if b**2 == a:
            div.append(b)
        if b**2 != a and a%b == 0:
            div.append(b)
            div.append(int(a/b))
        b += 1
    if a < sum(div):
        c = 2
        while c <= len(div):
            for d in combinations(div, c):
                if sum(d) == a:
                    s += 1    
            c += 1
        if s == 0:
            want.append(a)
if len(want) != 0:
    print(f'{number_1}~{number_2}の範囲で不思議数は{len(want)}個存在しそれらは以下の数である↓')
    e = want.pop(-1)
    for f in want:
        print(f, end = ', ')
    print(e)
else:
    print(f'{number_1}~{number_2}の範囲で不思議数は存在しない')                    