#互除法プログラム,最小公倍数、最大公約数算出プログラム
A = int(input('数を入力->'))
B = int(input('数を入力->'))
if B <= A:
    a = A
    b = B
    while True:
        c = a%b
        if c == 0: 
            d = int((A*B) / b)
            break
        a = b
        b = c
    print(str(A) + 'と' + str(B) + 'の最大公約数は' + str(b) + ', 最小公倍数は' + str(d))    
if A <= B:
    a = A
    b = B
    while True:
        c = b%a
        if c == 0:
            d = int((A*B) / a)
            break
        b = a
        a = c
    print(str(A) + 'と' + str(B) + 'の最大公約数は' + str(a) + ', 最小公倍数は' + str(d))
