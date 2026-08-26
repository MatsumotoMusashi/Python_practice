number = int(input('0以上の整数を入力->'))
n = 0
m = number
digit = []
if number != 0:
    while True:    
        if m != 0:
            while 2**n <= m:
                a = 2**n
                l = n
                n += 1
        digit.append(l)
        n = 0
        m -= a
        if m == 0:
            break
print(f'{number}を2進数表記すると以下のようになります↓')
if number != 0:
    two_exe = 0
    for x in digit:
        two_exe += 10**x
    print(f'{number}(2) = {two_exe}')
else:
    print(f'{number}(2) = 0')   