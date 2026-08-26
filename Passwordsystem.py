print('What is your name?')
name = str(input('>>'))
print('Hello' + ' ' + name + '')
print('Please input secret numbers')
i = 0
while i <= 10:
    # このプログラムはパスワードを入力した結果が適切か判断します
    a = int(input('input the numbers >>>'))
    b = str(a)
    print(b)
    if a == 1205:
        print('OK')
        break
    print('Something is wrong with the numbers')
    i = i + 1
if a != 1205:
    print('You are not' + ' ' + name)   