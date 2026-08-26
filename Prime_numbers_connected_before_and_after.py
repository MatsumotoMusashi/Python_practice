number = int(input('いくつまでの範囲で調べたいですか->'))
want = []
for a in range(1, number + 1):
    n = int(str(a) + str(a - 1))
    if len([b for b in range(1, n + 1) if n%b == 0]) == 2:
        want.append(a)
if len(want) != 0:
    print(f'{number}までの範囲でその数の1つ前の数とその数を連結した値が素数になる数は{len(want)}個ありそれらは以下の数です↓')
    c = want.pop(-1)
    for d in want:
        print(d, end = ', ')
    print(c)
else:
    print(f'{number}までの範囲では求めたい数は存在しませんでした')                