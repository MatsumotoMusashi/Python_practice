from fractions import Fraction
number_1 = int(input('初期値->'))
number_2 = int(input('最終値->'))
want = []
for a in range(number_1, number_2 + 1):
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
    div.sort()
    fra_m = 0
    for c in div:
        fra_m += Fraction(1, c)
    if int(len(div)/fra_m) == len(div)/fra_m:
        want.append(a)
if len(want) != 0:
    print(f'{number_1}~{number_2}の範囲で調和数は{len(want)}個存在しそれらは以下の数である↓')   
    d = want.pop(-1) 
    for e in want:
        print(e, end = ', ')
    print(d)
else:
    print(f'{number_1}~{number_2}の範囲で調和数は存在しない')            