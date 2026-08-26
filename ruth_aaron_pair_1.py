number = int(input('いくつまでの範囲で調べたいですか->'))
want = []
a = 1
while a + 1 <= number:
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
    j = 1
    div_2 = []
    prime_2 = []
    while j <= a + 1:
        if j in div_2:
            break
        if j**2 == a + 1:
            if len([c for c in range(1, j + 1) if j%c == 0]) == 2:
                prime_2.append(j)
        if j**2 != a + 1 and (a + 1)%j == 0:
            div_2.append(int((a + 1)/j)) 
            if len([c for c in range(1, j + 1) if j%c == 0]) == 2:
                prime_2.append(j)
            if len([c for c in range(1, int((a + 1)/j) + 1) if int((a + 1)/j)%c == 0]) == 2:
                prime_2.append(int((a + 1)/j))
        j += 1
    if sum(prime) == sum(prime_2):
        want.append((a, a + 1))
    a += 1
if len(want) != 0:
    print(f'{number}までの範囲でルース＝アロン・ペアは{len(want)}個存在しそれらは以下の数です↓')
    d = want.pop(-1)
    for e in want:
        print(e, end = ', ')
    print(d)
else:
    print(f'{number}までの範囲でルース＝アロン・ペアは存在しませんでした')        