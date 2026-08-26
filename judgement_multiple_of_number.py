Number = int(input('何の倍数の数を調べたいですか->'))
multiple_of_Number = []
not_multiple_of_Number = []
print('数の範囲を決定してください')
a = int(input('最初の数->'))
b = int(input('最後の数->'))
for x in range(a, b + 1):
    if x//Number == x/Number:
        multiple_of_Number.append(x)
    else:
        not_multiple_of_Number.append(x)
print(str(a) + 'から' + str(b) + 'までの範囲で' + str(Number) + 'の倍数は' + str(len(multiple_of_Number)) + '個ありそれらの数は以下の通りです↓')  
print(multiple_of_Number)
print(str(Number) + 'の倍数でない数は' + str(len(not_multiple_of_Number)) + '個ありそれらの数は以下の通りです↓')
print(not_multiple_of_Number)      