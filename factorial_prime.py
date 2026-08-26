number = int(input('いくつまで調べたいか->'))
if 2 < number:
    prime = [2]
    want_1 = [2]
    want_2 = []
elif number == 2:
    prime = [2]
    want_1 = [2]
    want_2 = []
else:
    prime = []
    want_1 = []
    want_2 = []
a = 3
while a <= number:
    can = 0
    for b in prime:
        if a%b == 0:
            can += 1 
    if can == 0:
        prime.append(a)
        c = a - 1
        d = a + 1
        e = 1
        fac_c = 1
        while True:
            fac_c *= e
            e += 1
            if c < fac_c*e or d <= fac_c*e:
                fac_d = fac_c*e
                break 
        if fac_c == c:
            want_1.append(a)    
        if fac_d == d:
            want_2.append(a)    
    a += 1            
if len(want_1) != 0:
    print(f'{number}まででn!+1型階乗素数は{len(want_1)}個存在しそれらは以下の数である↓')
    f = want_1.pop(-1)
    for g in want_1:
        print(g, end = ', ')
    print(f)
else:
    print(f'{number}までの範囲でn!+1型階乗素数は存在しない')
if len(want_2) != 0:
    print(f'{number}まででn!-1型階乗素数は{len(want_2)}個存在しそれらは以下の数である↓')                
    h = want_2.pop(-1)
    for i in want_2:
        print(i, end = ', ')
    print(h)    
else:
    print(f'{number}までの範囲でn!-1型階乗素数は存在しない')    