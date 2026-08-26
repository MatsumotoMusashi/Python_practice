#素因数分解プログラム
#エラトステネスの篩で素因数の可能性のある素数の洗い出し
Number = int(input('自然数を入力->'))
prime_number = []
eliminate_number = []
for number in (x for x in range(2, Number + 1)):
    if number not in eliminate_number:
        if Number%number == 0:
            prime_number.append(number)
            for y in (z for z in range(2, Number + 1)):
                if y%number == 0:
                    eliminate_number.append(y)
'''
素因数なら元の数を割り切れるという条件より素因数を求め、またその元の数を割りその商を再度その素因数で割り
割り切れなくなるまで続けその都度その素因数をリストに格納しそのリスト(factor_list)に格納されたその素因数
の個数(重複回数)が素因数分解でのその素因数の指数になる。
プログラム上発見された素因数は最初重複込みでリスト(factor_list)に格納されるが素因数自体は1つ見つかれば
いいので重複しないようにリスト(factor_list)から集合(prime_set)に保存していき重複しているものを取り除く。
最後にprime_number_divisionで素因数とその指数をタプルと言う形でバインドさせアンパッキングした時に素因数
とその指数が同時に出るようにする。
'''
a = Number
factor_list = []
for factor in prime_number:
    while a%factor == 0:
        a = int(a/factor)
        factor_list.append(factor)
prime_set = set()
for b in prime_number:
           prime_set.add(b)
prime_number_division = []
for c in prime_set:
     if factor_list.count(c) != 0:
         prime_number_division.append((c, factor_list.count(c)))
sorted(prime_number_division, key= lambda ero: ero[0])
print(f'{Number}を素因数分解すると以下のようになります↓')
for f in range(len(prime_number_division) - 1):
     g, h = prime_number_division[f]
     print(f'{g}^{h} × ', end = '')
i, j = prime_number_division[-1]
print(f'{i}^{j}')