#ゴールドバッハ予想再現プログラム
number = int(input('2以上の偶数を入力'))
prime_number = [a for a in range(1, number + 1) if len([z for z in (y for y in range(1, a + 1)) if a%z == 0]) == 2]
gold_prime = []
for b in prime_number:
    for c in prime_number:
        if b + c == number:
            gold_prime.append((b, c)) 
for d, e in gold_prime:
    if d != e:
        if (e, d) in gold_prime:
            gold_prime.remove((e, d))
'''
最初の出力でlen(number)+2の位置に「=」が表示される。
表示における「=」の位置を揃えたかったのでlen(number)+1の空白をfor文の繰り返しでの各出力の際に
表示させれば「=」の位置はlen(number)+2の位置に表示され「=」の位置を揃えることができる。
'''
go, nu = gold_prime[0]
print(f'{number} = {go} + {nu}')
del gold_prime[0]
for f, g in gold_prime:
    print(' '*(len(str(number)) + 1) + f'= {f} + {g}')