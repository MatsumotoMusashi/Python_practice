number = int(input('いくつまでの範囲(自然数範囲)で調べたいですか->'))
kapureka = []
for a in range(1, number + 1):
    if len(str(a**2)) == 1:
        if a**2 == a:
            kapureka.append(a)
    else:
        b = int(str(a**2)[:int(len(str(a**2))//2)])
        c = int(str(a**2)[int(len(str(a**2))//2):])
        if b != 0 and c != 0:
            if b + c == a:
                 kapureka.append(a)
if len(kapureka) == 0:
    print(f'{number}までの範囲でカプレカー数は存在しませんでした')
else:
    print(f'{number}までの範囲でカプレカー数は{len(kapureka)}個存在しそれらは以下の数です↓')
    d = kapureka.pop(-1)
    for e in kapureka:
        print(e, end = ', ')
    print(d)
