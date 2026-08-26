times = int(input('いくつの乱数を生成したいですか->'))
b = []
print('4つの異なる自然数を入力してください')
for a in range(4):
    number = int(input('Number:'))
    b.append(number)
M = max(b)
b.remove(M)
A = b[0]
B = b[1]
x_1 = b[2]
for c in range(times):
    x_2 = ((A*x_1) + B)%M
    print(x_2)
    x_1 = x_2