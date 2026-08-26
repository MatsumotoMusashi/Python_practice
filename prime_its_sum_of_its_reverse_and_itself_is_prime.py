'''
reverseのリストに指定範囲内の素数とその素数を反転させた数の和を入れcopyのリストに指定範囲内で発見された
素数のデータを保存しておく。
primeのリストにはreverseのリスト内の要素の最大値以下の素数をすべて保存しておく。
こうすることでprimeのリストにはreverseのリスト内の素数すべてが含まれることになる。
reverse内の最大値をaとすると、reverse内の素数はa以下でprimeにはa以下の素数がすべて含まれているので
reverse内の素数は全てprimeに含まれている。
故に指定範囲内の素数を一つずつ取り出しその素数とその素数自身を反転させた数の和のうち素数のもの
(=reverseのリスト内の素数)は全てprimeのリストに含まれている。
指定範囲内の素数を一つずつ取り出しその素数とその素数自身を反転させた数の和(reverseのリスト内の数)が
素数ならprimeのリストに含まれている(if d + int(str(d)[::-1]) in prime: がTrueとなる)ので、
if d + int(str(d)[::-1]) in prime: がTrueとなるならその和は素数であるためその和に対応する素数は
欲しい素数なのでwantのリストに入れる。
こうすることで一つ一つに対して素数判定する必要がなくなる(1000レベルの繰り返しをせずに済む)ので計算量を
減らせるのではないか。
'''
number = int(input('いくつまで調べたいか->'))
if 2 < number: 
    prime = [2]
    reverse = [4]
    want = []
elif number == 2:
    prime = [2]
    reverse = [4]
    want = []
else:
    prime = []
    reverse = []
    want = []
a = 3
if 3 <= number:
    while a <= number:
        can = 0
        for b in prime:
            if a%b == 0:
                can += 1       
        if can == 0:
            prime.append(a)
            reverse.append(a + int(str(a)[::-1]))
        a += 1
    copy = prime.copy()    
    while a <= max(reverse):
        can = 0
        for c in prime:
            if a%c == 0:
                can += 1
        if can == 0:
            prime.append(a)
        a += 1            
    for d in copy:
        if d + int(str(d)[::-1]) in prime:
            want.append(d)
if len(want) != 0:
    print(f'{number}までの範囲で素数とその素数自身を反転させた数の和が素数となる素数は{len(want)}個存在しそれらは以下の数である↓')
    e = want.pop(-1)
    for f in want:
        print(f, end = ', ')
    print(e)
else:
    print(f'{number}までの範囲で素数とその素数自身を反転させた数の和が素数となる素数は存在しない')                