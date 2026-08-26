number = int(input('いくつの階乗を求めたいですか->'))
sum = 1
for a in range(2, number + 1):
    sum *= a
print(f'{number}! =  {sum}')    