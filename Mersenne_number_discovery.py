number = int(input('いくつまでの範囲を調べたいですか>'))
index = []
Mersenne_number = []
for x in range(1, number + 1):
    y = x + 1
    while (y)%2 == 0:
        index.append(2)
        y = y/2
    if 2**(index.count(2)) - 1 == x:
        Mersenne_number.append(x)
    index = []
Mersenne_prime = [y for y in Mersenne_number if len([a for a in (z for z in range(1, y + 1)) if y%a == 0]) == 2]
if len(Mersenne_number) != 0:
    print(f'{number}までの範囲で見つかったメルセンヌ数は{len(Mersenne_number)}個でそれらは以下の数です↓')
    me = Mersenne_number[-1]
    del Mersenne_number[-1]
    for b in Mersenne_number:
        print(b, end = ', ')
    print(me)
    if len(Mersenne_prime) != 0:                
        print(f'{number}までの範囲でメルセンヌ素数は{len(Mersenne_prime)}個ありそれらは以下の数です↓')
        me_pr = Mersenne_prime[-1]
        del Mersenne_prime[-1]
        for c in Mersenne_prime:
            print(c, end = ', ')
        print(me_pr)
    else:
        print(f'{number}までの範囲でメルセンヌ素数は存在しません')    
else:
    print(f'{number}までの範囲でメルセンヌ数は存在しません')            