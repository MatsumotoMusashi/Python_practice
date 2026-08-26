number = int(input('自然数を入力->'))
index = int(input(f'{number}の平方根の近似値を小数第何位まで求めたいですか->'))
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
'''
bに該当する値は前の操作で求めた値でよいのでbに上書きしていく。
bが小数点以下2桁ならcは小数点以下3桁にしたいので10**c, c += 1でbの小数点以下の桁数より1桁多くしている
'''    