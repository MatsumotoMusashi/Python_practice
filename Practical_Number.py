from itertools import combinations
number_1 = int(input('初期値:'))
number_2 = int(input('終了値:'))
want = []
print('数の途中経過↓')
for a in range(number_1, number_2 + 1):
    print(a)
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
    b += 1 
    need = set()
    p = []
    for c in range(2, len(div) + 1):
        for d in combinations(div, c):
            p.append(d)        
        need.add(div[c - 2])
    for i in range(1, a):
        if i not in div:
            for e in p:
                s = 0
                for f in e:
                    s += f
                if s == i:
                    need.add(i)
    if len(need) == a - 1:
        want.append(a)
if len(want) != 0:
    print(f'{number_1}~{number_2}の範囲でプラクティカル数は{len(want)}個存在しそれらは以下の数である↓')
    h = want.pop(-1)
    for j in want:
        print(j, end = ', ')
    print(h)
else:
    print(f'{number_1}~{number_2}の範囲でプラクティカル数は存在しない')        