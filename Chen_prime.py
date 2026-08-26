'''
指定範囲で発見された最後の素数をpとしたときp + 2が素数であったときのためにprimeのリストは
p + 2以上の素数が1個以上含まれている必要がある。そのため指定範囲を超えた後の素数発見の終了
条件はpと指定範囲外で発見された素数の差が2以上となったとき終了とした(2 <= a - p_c[-1])。
よってpよりも2以上大きい素数が発見されたとき素数探索を終了しているためprimeには必ずpよりも
2以上大きい素数が一つ含まれている。
このことでp_cのリストの範囲内にある素数(指定範囲内で発見された素数)に2を加えた数は全てprime[-1]
の値以下となる。
仮にp_cリストの素数に2を加えた数が素数であった場合上記の前提事実からprimeに含まれているはずである。
逆に合成数なら含まれない。
故にp_cリストの各素数に2を加えた数が素数かどうかの判定はその数がprimeのリストに含まれているかどうか
で判定できる。(if (d + 2) in prime:)
半素数とは二つの素数(同じ素数でもよい)の積であらわせられ素数p,qを用いてp*qと表せられる(p = qもOK)。
故に半素数の素因数は1~2種類であるので素因数が3種類以上であれば半素数ではない。
半素数で素因数が1種類のときその素因数の二乗が元の数(その素因数を有する数)と等しければ半素数、
そうでなければその素数同士の3個以上の積またはその素因数自体が元の数となるため半素数ではない。
2種類の時はその2種類の素因数の積(各素因数の指数は1)と等しければ半素数、そうでなければ両方または一方の
素因数の指数が2以上であるため最低でも同種のもの2個ともう一方の素因数の積、即ち3個の素数の積となるため
半素数とはならない。
'''
number = int(input('いくつまで調べたいか->'))
if 2 < number:
    prime = [2] 
elif number == 2:
    prime = [2]
    p_c = prime.copy()
want = []
a = 3
s = ''
if number != 1:
    while True:
        while a <= number:
            can = 0
            for b in prime:
                if a%b == 0:
                    can += 1
            if can == 0:
                prime.append(a)
                p_c = prime.copy()
            a += 1
        can = 0
        for c in prime:
            if a%c == 0:
                can += 1
        if can == 0:
            prime.append(a)
            if 2 <= a - p_c[-1]:
                s = 'OK'
        if s == 'OK':
            break
        a += 1                
    for d in p_c:
        if (d + 2) in prime:
            want.append(d)
        else:
            e = 1
            div = []
            pr_div = []
            while e <= d + 2:
                if e in div:
                    break
                if e**2 == d + 2:
                    div.append(e)
                    if e in prime:
                        pr_div.append(e)
                elif (d + 2)%e == 0:
                    div.append(e)
                    div.append(int((d + 2)/e))
                    if e in prime:
                        pr_div.append(e)
                    if int((d + 2)/e) in prime:
                        pr_div.append(int((d + 2)/e))
                e += 1 
            if len(pr_div) == 1:
                if (pr_div[0])**2 == d + 2:
                    want.append(d)
            elif len(pr_div) == 2:
                if (pr_div[0])*(pr_div[1]) == d + 2:
                    want.append(d)        
if len(want) != 0:
    print(f'{number}までの範囲で陳素数は{len(want)}個存在しそれらは以下の数である↓')
    k = want.pop(-1)
    for j in want:
        print(j, end = ', ')
    print(k)
else:
    print(f'{number}までの範囲で陳素数は存在しない')        