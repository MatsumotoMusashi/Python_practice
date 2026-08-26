#フェルマー数の発見プログラム
number = int(input('いくつまでの範囲(自然数)でフェルマー数を調べたいですか->'))
Fermat_number = []
l = 0
m = 0
if 3 <= number:
    for a in range(2, number + 1):
        b = a - 1
        while b%2 == 0:
            b = b/2
            l += 1
            if 2**(l) + 1 == a:
                c = l
                while c%2 == 0:
                   c = c/2
                   m += 1
                   if 2**(m) == l:
                       Fermat_number.append(a)
        l = 0
        m = 0
    print(f'{number}までで{len(Fermat_number) + 1}個のフェルマー数がありそれらは以下の数です↓')
    if len(Fermat_number) != 0:
        print(3, end = ', ')
        fer = Fermat_number[-1]
        del Fermat_number[-1]
        for d in Fermat_number:
            print(d, end = ', ')
        print(fer)
    else:
        print(3)
else:
    print(f'{number}まででフェルマー数は存在しません')    