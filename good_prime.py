'''
良い素数かどうかを判定するにはn番目の素数を発見してから新たに最大n-1個の素数を発見する必要がある。
指定した範囲で最後の素数を発見してからその素数の番目(e = len(prime)のe)-1、即ちe - 1個の素数を
新たに発見できるまで繰り返す。while Trueの繰り返しは新たに発見された素数の個数sがe - 1と等しく
なった時(s = e - 1)終了する(break)
また調査対象の素数はp_cに、必要な長さまでそろえた素数数列はprimeに保存した。これはprimeでやって
しまうと調査対象外の素数(指定範囲外の素数)まで調べてしまうため計算量が増え無意味な動作でまた
prime[n + g -1]が存在しない事態が発生してしまいエラーが生じるためエラーを防ぐ観点から調査対象の
素数リストp_cと良い素数かどうか判定するための素数リストprimeに分ける必要がある。
'''
number = int(input('いくつまでの範囲で調べたいか->'))
if number != 1:
    prime = [2]
else:
    prime = []
want = []
a = 3
s = 0
if 3 <= number: 
    while True:
        while a <= number:
            can = 0
            for b in prime:
                if a%b == 0:
                    can += 1
            if can == 0:
                prime.append(a)
                e = len(prime)
                p_c = prime.copy()
            a += 1
        can = 0
        for c in prime:
            if a%c == 0:
                can += 1
        if can == 0:
            prime.append(a)
            s += 1
        if s == e - 1:
            break
        a += 1
    for f in p_c:
        out = 0
        n = prime.index(f) + 1
        if 2 <= n:
            for g in range(1, n):
                if f**2 <= (prime[n - g - 1])*(prime[n + g - 1]):
                    out += 1
            if out == 0:
                want.append(f)      
if len(want) != 0:
    print(f'{number}までの範囲で良い素数は{len(want)}個存在しそれらは以下の数である↓')
    h = want.pop(-1)
    for j in want:
        print(j, end = ', ')
    print(h)
else:
    print(f'{number}までの範囲で良い素数は存在しない')        