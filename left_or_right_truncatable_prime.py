number = int(input('いくつまでの範囲で調べたいか->'))
prime = set()
if 2 <= number:
    prime.add(2)
want_1 = []
want_2 = []
for a in range(2, number + 1):
    can = 0
    for b in prime:
        if a%b == 0:
            can += 1
    if a == 2 or can == 0:
        prime.add(a)
        out_1 = 0
        out_2 = 0
        d = [c for c in str(a)]
        if '0' not in d:
            for e in range(1, len(str(a))):
                if int(str(a)[e:]) not in prime:
                    out_1 += 1
                if int(str(a)[:-e]) not in prime:
                    out_2 += 1    
            if out_1 == 0:
                want_1.append(a)        
            if out_2 == 0:
                want_2.append(a)    
if 2 <= number:               
    print(f'{number}までの範囲で左切り捨て可能素数は{len(want_1)}個存在しそれらは以下の数である↓')
    f = want_1.pop(-1)
    for g in want_1:
        print(g, end = ', ')
    print(f)
    print('-'*119)    
    print(f'{number}までの範囲で右切り捨て可能素数は{len(want_2)}個存在しそれらは以下の数である↓')
    h = want_2.pop(-1)
    for i in want_2:
        print(i, end = ', ')
    print(h)            
else:
    print(f'{number}までの範囲で左切り捨て可能素数は存在しない')
    print(f'{number}までの範囲で右切り捨て可能素数は存在しない')    