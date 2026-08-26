'''
素数と判定された数から1を引いた数(a - 1)が指数が非負整数の2と3の積のみであらわせるかどうかを判定する。
a - 1を2,3で割り切れた回数をl.20~l.29の過程で求める。
もしaがピアポント素数ならばa - 1と2,3の各指数をa - 1を2,3で割り切れた回数とした
(2**digit_2)*(3**digit_3)という積と等しくなるはずである。(if (2**digit_2)*(3**digit_3) == a - 1)
等しくなければa - 1の素因数が2,3以外、もしくはa - 1が2,3以外にも素因数をもつため等しくならないのであろう。
'''
number = int(input('いくつまで調べたいか->'))
if 2 <= number:
    prime = [2]
    want = [2]
else:
    prime = []
    want = []
a = 3
while a <= number:
    can = 0
    for b in prime:
        if a%b == 0:
            can += 1
    if can == 0:
        prime.append(a)
        c = a - 1
        digit_2 = 0
        while c%2 == 0:
            digit_2 += 1
            c = int(c/2)
        c = a - 1
        digit_3 = 0
        while c%3 == 0:
            digit_3 += 1
            c = int(c/3)
        if (2**digit_2)*(3**digit_3) == a - 1:
            want.append(a)
    a += 1
if len(want) != 0:
    print(f'{number}までの範囲でピアポント素数は{len(want)}個存在しそれらは以下の数である↓')
    d = want.pop(-1)
    for e in want:
        print(e, end = ', ')
    print(d)
else:
    print(f'{number}までの範囲でピアポント素数は存在しない')                    