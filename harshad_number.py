ran = int(input('いくつまでの範囲(自然数範囲)を調べたいか->'))
h = []
for a in range(1, ran + 1):
    i = 1
    eliminate = []
    division = []
    while i <= a:
        if i in eliminate:
            break
        if i**2 == a:
            division.append(i)
            eliminate.append(i)
        if i**2 != a and a%i == 0:
            division.append(i)
            division.append(int(a/i))
            eliminate.append(int(a/i))
        i += 1
    if sum([int(b) for b in str(a)]) in division:
        h.append(a)
if len(h) == 0:
    print(f'{ran}までの範囲でハーシャッド数は存在しない')
else:
    print(f'{ran}までの範囲でハーシャッド数は{len(h)}個ありそれらは以下の数です↓')
    d = h.pop(-1)
    for e in h:
        print(e, end = ', ')
    print(d)                