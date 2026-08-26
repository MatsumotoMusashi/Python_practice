number = int(input('いくつまで調べたいか->'))
want = []
for a in range(1, number + 1):
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
    if int(str(sum(div))[::-1]) == sum(div):
        want.append(a)
if len(want) != 0:
    print(f'{number}までの範囲で約数の和が回文数になる数は{len(want)}個存在しそれらは以下の数である↓')
    c = want.pop(-1)
    for d in want:
        print(d, end = ', ')
    print(c)
else:
    print(f'{number}までの範囲で約数の和が回文数になる数は存在しない')               