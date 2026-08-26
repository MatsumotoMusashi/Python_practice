Number = int(input('自然数を入力->'))
divisor_list = []
for x in range(1, Number + 1):
    if Number%x == 0:
        divisor_list.append(x)
print(str(Number) + 'の約数は' + str(len(divisor_list)) + '個でそれらは以下の数です↓')
print(divisor_list)
sum = 0
for y in divisor_list:
    sum += y        
print(str(Number) + 'の約数の総和:', sum)    