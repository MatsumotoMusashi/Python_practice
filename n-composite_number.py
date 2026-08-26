number = int(input('いくつまでの範囲(自然数範囲)で調べたいか->'))
n = int(input('いくつの素数の積で表わされる合成数を調べたいか->'))
want = []
for a in range(1, number + 1):
    i = 1
    division = []
    while i <= a:
        if i in division:
            break
        if i**2 == a:
            division.append(i)
        if i**2 != a and a%i == 0:
            division.append(i)
            division.append(int(a/i))
        i += 1
    prime = []
    for b in division:
        j = 1
        div = []
        while j <= b:
            if j in div:
                break
            if j**2 == b:
                div.append(j)
            if j**2 != b and b%j == 0:
                div.append(j)
                div.append(int(b/j))
            j += 1     
        if len(div) == 2:
            prime.append(b)       
    if len(prime) == n:
        index = []
        for c in prime:
            m = a
            d = 0
            while m%c == 0:
                m = int(m/c)
                d += 1
            index.append(d)
        if sum(index) == len(prime):
            want.append(a)                
if len(want) == 0:
    print(f'{number}までの範囲で{n}素合成数は存在しません')
else:     
    print(f'{number}までの範囲で{n}素合成数は{len(want)}個存在しそれらは以下の数です↓')    
    e = want.pop(-1)
    for f in want:
        print(f, end = ', ')
    print(e)    