a = int(input('0以上の整数を入力->'))
b = int(input('何乗根を調べたいか->'))
number = []
for x in range(-a, a+1):
    if x**b == a:
        number.append(x)
if len(number) > 0:
    print(str(a) + 'の整数の' + str(b) + '乗根は以下の整数です↓')
    for y in number:
        print(y, end = ' ')
else:        
    print(str(a) + 'の' + str(b) + '乗根に整数のものは存在しませんありません')