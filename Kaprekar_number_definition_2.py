number = int(input('いくつ(自然数範囲)まで調べたいか->'))
kapureka = []
for a in range(1, number + 1):
    b = [c for c in str(a)]
    minimum = int(''.join(sorted(b)))
    maximum = int(''.join(sorted(b, reverse = True)))
    if maximum - minimum == a:
        kapureka.append(a)
if len(kapureka) == 0:
    print(f'{number}までの範囲でカプレカー数は存在しない')
else:
    print(f'{number}までの範囲でカプレカー数は{len(kapureka)}個ありそれらは以下の数です↓')
    d = kapureka.pop(-1)
    for e in kapureka:
        print(e, end = ', ')
    print(d)    