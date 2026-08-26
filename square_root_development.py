number = int(input('自然数を入力->'))
index = int(input(f'{number}の平方根の近似値を小数第何位まで求めたいですか->'))
'''
number_1は√61000などの平方根を求める際に√61000 = √610*10 と計算できるので
√610のみを求めてそれに10をかけて√61000を求めるなどして計算量を減らしている
number_2は√6100などの平方根を求める際に√6100 = √61*10と計算できるので
√61のみを求めてそれに10をかけて√6100を求めるなどして計算量を減らしている
どちらも共通してくくりだして求める平方根はくくりだした10**nの2乗でnumber
を割った数の平方根となっている
例えば√61000で求める√610の610は61000/((10**1)**2) (->n=1のとき)より計算して得られる
大きいif節では10についてくくりだしをしている
10以外のくくりだしまで一般化するのはまた後日考えよう

'''
if number%10 == 0:
    x = number
    ten_index = 0
    while x%10 == 0:
        ten_index += 1
        x = x/10
    if ten_index%2 != 0: 
        number_1 = int(number/(10**(ten_index -1)))
        ten_index -= 1       
        b = max([a for a in range(number_1 + 1) if a**2 <= number_1])
        c = 1
        while c <= index + (ten_index/2):
            b = max([float(format((b + (d/(10**c))), f'.{c}f')) for d in range(10) 
                     if float(format(((b + (d/(10**c)))**2), f'.{c}f')) <= number_1])
            c += 1
        b = float(format(b*(10**(ten_index/2)), f'.{index}f'))    
        print(f'{number}の平方根の小数第{index}位までの近似値は以下の値です')
        print(f'√{number} = {b}')
    else:
        number_2 = int(number/(10**ten_index))
        b = max([a for a in range(number_2 + 1) if a**2 <= number_2])
        c = 1
        if b**2 != number_2:
            while c <= index + (ten_index/2):
                b = max([float(format((b + (d/(10**c))), f'.{c}f')) for d in range(10) 
                         if float(format((b + (d/(10**c)))**2, f'.{c}f')) <= number_2])
                c += 1
            b = float(format(b*(10**(ten_index/2)), f'.{index}f'))
            print(f'{number}の平方根の小数第{index}位までの近似値は以下の値です')
            print(f'√{number} = {b}')
        else:
            print(f'{number}の平方根の小数第{index}位までの近似値は以下の値です')
            print(f'√{number} = ' + format(10**(ten_index/2), f'.{index}f'))
else:
    b = max([a for a in range(number + 1) if a**2 <= number])
    if b**2 == number:
        print(f'{number}の平方根の小数第{index}位までの近似値は以下の値です')
        print(f'√{number} = ', format(b, f'.{index}f'))
    else:    
        c = 1
        while c <= index:
            b = max([float(format((b + (d/(10**c))), f'.{c}f')) for d in range(10) 
                     if float(format((b + (d/(10**c)))**2, f'.{c}f')) <= number])
            c += 1
        print(f'{number}の平方根の小数第{index}位までの近似値は以下の値です')
        print(f'√{number} = {b}')