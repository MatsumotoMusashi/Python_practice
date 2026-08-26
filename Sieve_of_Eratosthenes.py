'''
prime_numberには素数のみを登録したい。
numberが素数の倍数なら調べない、素数なら調べるようにするために(numberが素数の倍数ならその倍数が
素数であることはなくまた素数が出た時点で判定できているので調べる必要なし)
numberがeliminate_number中にあるか
即ち素数の倍数か判定し、そうでなければprime_numberに登録しその素数の倍数をeliminate_numberにまとめて
次以降に出てくるその素数の倍数は調べないようにして篩にかける
(removeメッソドは調べたいインデックスが動くので2を除去すると3が0インデックスに移り3がnumberに代入されず困る)
'''
a = int(input('いくつの数まで調べたいですか->'))
Number_list = [x for x in range(2, a + 1)]
prime_number = []
eliminate_number = []
for number in Number_list:
    if number not in eliminate_number:
        prime_number.append(number)
        for y in Number_list:
            if y%number == 0:
                eliminate_number.append(y)        
print('1から' + str(a) + 'までの範囲に素数は' + str(len(prime_number)) + '個ありそれらは以下の数です↓')
print(prime_number)            
