#平方根の括り出しのプログラム
number = int(input('整数を入力->'))
if number < 0:
    a = -number
else:
    a = number
div = []
prime = []
b = 1
while b <= a:
    if b in div:
        break
    if b**2 == a:
        div.append(b)
        if len([c for c in range(1, b + 1) if b%c == 0]) == 2:
           prime.append(b)
    elif a%b == 0:
        div.append(b)
        div.append(int(a/b)) 
        if len([c for c in range(1, b + 1) if b%c == 0]) == 2:
            prime.append(b)
        if len([c for c in range(1, int(a/b) + 1) if int(a/b)%c == 0]) == 2:
            prime.append(int(a/b))                  
    b += 1
f = []
for e in prime:
    d = a
    digit = 0
    while d%e == 0:
        d = int(d/e)
        digit += 1
    f.append((e, digit))
j = []
k = []
for g, h in f:
    i = 0
    while i <= h:
        i += 2
    j.append((g, int((i - 2)/2)))
    k.append((g, (h - i + 2)))
keisuu = 1
for l, m in j:
    keisuu *= l**m
naka = 1
for n, o in k:
    naka *= n**o
if number < 0:
    if naka == 1:
        if keisuu == 1:
            keisuu = ''    
        print(f'±√{number} = ±{keisuu}i')
    else:    
        if keisuu == 1:
            keisuu = ''
        print(f'±√{number} = ±{keisuu}√{naka}i')
elif 0 < number:
    if naka ==1:
        print(f'±√{number} = ±{keisuu}')
    else:
        if keisuu == 1:
            keisuu = ''
        print(f'±√{number} = ±{keisuu}√{naka}')    
else:
    print(f'±√{number} = 0')        