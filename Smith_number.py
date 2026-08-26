number = int(input('いくつまで調べたいか->'))
smith = []
for a in range(1, number + 1):
    i = 1
    prime = []
    division = []
    while i <= a:
        if i in division:
            break
        if i**2 == a:
            b = 1
            div = []
            while b <= i:
                if b in div:
                    break
                if b**2 == i:
                    div.append(b)
                if b**2 != i and i%b == 0:
                    div.append(b)
                    div.append(int(i/b))
                b += 1    
            if len(div) == 2:
                prime.append(i)
            division.append(i)                
        if i**2 != a and a%i == 0:
            b = 1
            div = []
            while b <= i:
                if b in div:
                    break
                if b**2 == i:
                    div.append(b)
                if b**2 != i and i%b == 0:
                    div.append(b)
                    div.append(int(i/b))
                b += 1    
            if len(div) == 2:
                prime.append(i)
            division.append(i)    
            b = 1
            div = []
            while b <= int(a/i):
                if b in div:
                    break
                if b**2 == int(a/i):
                    div.append(b)
                if b**2 != int(a/i) and int(a/i)%b == 0:
                    div.append(b)
                    div.append(int(int(a/i)/b))
                b += 1    
            if len(div) == 2:
                prime.append(int(a/i))
            division.append(int(a/i)) 
        i += 1
    if 2 < len(division):       
        dig_prime = []
        k = []
        n = a
        for f in prime:
            ti = 0
            while n%f == 0:
                ti += 1
                n = int(n/f)
            dig_prime.append((f, ti))   
            k.append(ti) 
        if sum(k) == len(prime):
            dig_1 = 0
            for c in prime:
                dig_2 = 0
                for d in str(c):
                    dig_2 += int(d)
                dig_1 += dig_2
            dig_a = 0
            for e in str(a):
                dig_a += int(e)
            if dig_a == dig_1:
                smith.append(a)
        else:
            dig_1 = 0
            for c, d in dig_prime:
                dig_2 = 0
                for h in str(c):
                    dig_2 += int(h)
                dig_1 += dig_2*d
            dig_a = 0
            for e in str(a):
                dig_a += int(e)
            if dig_a == dig_1:
                smith.append(a)                                
if len(smith) == 0:
    print(f'{number}までの範囲でスミス数は存在しません')
else:
    print(f'{number}までの範囲でスミス数は{len(smith)}個ありそれらは以下の数です↓')
    x = smith.pop(-1)
    for y in smith:
        print(y, end = ', ')
    print(x)