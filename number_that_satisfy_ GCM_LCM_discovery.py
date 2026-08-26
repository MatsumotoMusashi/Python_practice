g = int(input('最大公約数を入力->'))
l = int(input('最小公倍数を入力->'))
number_1 = []
for a in range(1, (g*l) + 1):
    for b in range(1, (g*l) + 1):
        if a*b == g*l:
            number_1.append((a, b))            
for c, d in number_1:
    if c != d:
        if (d, c) in number_1:
            number_1.remove((d, c))
number_2 = []
for e, f in number_1:
    h = e
    i = f
    while True:
        j = i%h
        if j == 0:
            k = int((e*f) / h)
            break
        i = h
        h = j 
    if h == g and k == l:
        number_2.append((e, f))
if len(number_2) != 0:        
    print(f'最大公約数が{g}、最小公倍数が{l}の2数は{len(number_2)}組ありそれらは以下の組です↓')
    num, ber = number_2[-1]
    del number_2[-1]
    for x, y in number_2:
        print(f'{x}と{y}', end = ', ')
    print(f'{num}と{ber}')    
else:
    print(f'最小公倍数が{g}、最大公約数が{l}の2数は存在しません')     