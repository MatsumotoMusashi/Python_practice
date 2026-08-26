number = int(input('いくつまでの範囲で調べたいか->'))
prime = [2]
want = []
for a in range(3, number + 1):
    can = 0
    for b in prime:
        if a%b == 0:
            can += 1
    if can == 0:
        prime.append(a)
        if (prime.index(a) + 1) in prime:
            want.append(a)
if len(want) != 0:
    print(f'{number}までの範囲でスーパー素数は{len(want)}個存在しそれらは以下の数である↓') 
    c = want.pop(-1)
    for d in want:
        print(d, end = ', ') 
    print(c)          
else:
    print(f'{number}までの範囲でスーパー素数は存在しない')