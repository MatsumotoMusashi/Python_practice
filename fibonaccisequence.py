c = 1
d = 2
n = int(input('いくつまでの範囲でフィボナッチ数を調べる==>'))
print('第1項', c)
print('第2項', d)
a = 3
l = 0
while l <= n:    
    l = d + c
    c = d
    d = l
    while l <= n:        
        print('第' + str(a) + '項', l)
        a = a + 1
        break