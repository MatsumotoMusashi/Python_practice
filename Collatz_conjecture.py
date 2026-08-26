n = int(input('number:'))
if n == 1:
    print('1->4->2->1')
else:
    a_n = []
    a_n.append(n)
    while n != 1:
        if n%2 == 0:
            n = int(n/2)
            a_n.append(n)
        else:
            n = 3*n + 1
            a_n.append(n)
    c = a_n.pop(-1)
    for b in a_n:
        print(f'{b}->', end = '') 
    print(c)