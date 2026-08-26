Number_1 = int(input('自然数を入力->'))
Number_2 = int(input('自然数を入力->'))
Number_3 = int(input('自然数を入力->'))
divisor_Number_1 = [x for x in range(1, Number_1 + 1) if Number_1%x == 0]
divisor_Number_2 = [y for y in range(1, Number_2 + 1) if Number_2%y == 0]
divisor_Number_3 = [z for z in range(1, Number_3 + 1) if Number_3%z == 0]
common_divisor = [a for a in divisor_Number_1 if a in divisor_Number_2 and a in divisor_Number_3]
print(str(Number_1) + ', ' + str(Number_2) + ', '+ str(Number_3) 
      + 'の公約数は' + str((len(common_divisor))) + '個あり、それらは以下の数です↓')
for b in range(len(common_divisor) - 1):
    print(str(common_divisor[b]) + ', ', end = '')
print(common_divisor[-1])

