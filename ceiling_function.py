number = float(input('NUmber:'))
a = 0
if number <= 0:
    while number <= a:
        a -= 1
    if int(number) == number:
        print(f'ceil({int(number)}) = {a + 1}')
    else:
        print(f'ceil({number}) = {a + 1}')        
else:
    while a < number:
        a += 1
    if int(number) == number:
        print(f'ceil({int(number)}) = {a}')
    else:
        print(f'ceil({number}) = {a}')                