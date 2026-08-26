#約数発見プログラム
number = int(input('自然数を入力->'))
x = 1
division_number = []
eliminate_number = []
while x <= number:
    if x**2 == number:
        division_number.append(x)
    if number%x == 0 and x**2 != number:
        division_number.append(x)
        division_number.append(int(number/x))
        eliminate_number.append(int(number/x))
    x += 1
    if x in eliminate_number:
        break       
division_number.sort()
copy = division_number.copy()
print(f'{number}の約数は{len(division_number)}個ありそれらは以下の数です↓')
a = division_number.pop(-1)
for b in division_number:
    print(b, end = ', ')
print(a)        
#素因数分解プログラム
del copy[0]
prime_division = []
for y in copy:
    n = 1
    sum = 0
    elimi_number = []
    while n <= y:
        if n**2 == y:
            sum += 1
        if y%n == 0 and n**2 != y:
            sum += 2
            elimi_number.append(int(y/n))
        n += 1
        if n in elimi_number:
            break
    if sum == 2:
       prime_division.append(y)
if len(division_number) + 1 > 2:
    print(f'{number}を素因数分解すると以下のようになります↓')
    factor = []
    for z in prime_division:
            nu = number
            i = 0
            while nu%z == 0:
                i += 1
                nu = int(nu/z)
            factor.append((z, i))
    f, g = factor.pop(-1)
    print(f'{number} = ', end = '')
    for d, e in factor:
        if e != 1:
            print(f'{d}^{e} × ', end = '')
        else:
            print(f'{d} × ', end = '')    
    if g != 1:
        print(f'{f}^{g}')
    else:
        print(f'{f}')
elif len(division_number) + 1 == 2:
    print(f'{number}は素数です')
else:
    print(f'{number}は素因数分解できません')