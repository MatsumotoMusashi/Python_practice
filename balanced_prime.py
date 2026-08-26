'''
指定した範囲の素数すべてに対して平衡素数かどうかを判定するには最後に発見される素数の次の素数まで求める
必要がある。最後の素数が平衡素数かどうか判定するにはその素数の一個前の素数は指定範囲内だが次の素数は
指定範囲外となってしまうため最後の素数の次の素数を発見するために指定範囲を超えて1つ次の素数を発見
しておく必要がある。その操作を実現するのがl.14~l.33のwhile文のネスト構造である。
指定範囲を超えれば(a > number)指定範囲の素数発見プログラム(while a <= numberの節)は実行されずその下
に書かれているプログラムが指定範囲の最後の素数の次の素数を発見するまで(while a <= numberの繰り返しが
終了してから発見された素数の個数が1個となる(s == 1)まで)繰り返される。
'''
number = int(input('いくつまで調べたいか->'))
if number != 1:
    prime = [2]
else:
    prime = []
a = 3
want = []
while True:
    while a <= number:
        can = 0
        for b in prime:
            if a%b == 0:
                can += 1
        if can == 0:
            prime.append(a)
        a += 1 
    s = 0
    can = 0
    for b in prime:
        if a%b == 0:
            can += 1
    if can == 0:
        prime.append(a)
        s += 1
    if s == 1:
         break            
    a += 1    
if 3 <= len(prime):
    i = 1
    while i + 1 <= len(prime) - 1:
        if prime[i] == (prime[i - 1] + prime[i + 1])/2:
            want.append(prime[i])
        i += 1
if len(want) != 0:
    print(f'{number}までの範囲で平衡素数は{len(want)}個存在しそれらは以下の数である↓')
    j = want.pop(-1)
    for k in want:
        print(k, end = ', ')
    print(j)
else:
    print(f'{number}までの範囲で平衡素数は存在しない')                