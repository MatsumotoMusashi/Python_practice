print('数の範囲を入力')
a = int(input('最初の数:'))
b = int(input('最後の数:'))
copy = a
c = []
c_copy = []
if a == 1:
    c.append((1, 4))
    c_copy.append(4)
    a += 1
if a != 1:
    while a <= b:
        d = a
        a_n = []
        a_n.append(a)
        while a != 1:
            if a%2 == 0:
                a = int(a/2)
                a_n.append(a)
            else:
                a = 3*a + 1
                a_n.append(a)
        a = d
        c.append((a, len(a_n)))
        c_copy.append(len(a_n))
        a += 1
e = max(c_copy) 
g = sorted(c, key = lambda f: f[1], reverse = True)
h = 0
k = []
while True:
    i, j = g[h]
    if j != e:
        break
    k.append(i)
    h += 1
print(f'{copy}~{b}までの範囲で以下の数から始まるときコラッツ数列の項数は最大になります')
k.sort()
l = k.pop(-1)
for m in k:
    print(m, end = ',')
print(f'{l}から始まるときコラッツ数列の項数は{e}項あります')    