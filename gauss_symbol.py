number = float(input('ガウス記号を適用する数を入力してください->'))
a = 0
if number == 0:
    print(f'[{int(number)}] = {a}')
elif number > 0:
    while a <= number:
        a += 1
    if number == int(number):
        print(f'[{int(number)}] = {a - 1}')
    else:
        print(f'[{number}] = {a - 1}')    
else:
    while True:
        if a <= number:
            break
        a -= 1
    if number == int(number):    
        print(f'[{int(number)}] = {a}')
    else:
        print(f'[{number}] = {a}')        