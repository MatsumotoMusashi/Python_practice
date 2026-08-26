#ナルシシスト数の判定プログラム
number = int(input('自然数を入力:'))
number_division = [int(x)**len(str(number)) for x in str(number)]
if number == sum(number_division):
    print(f'{number}はナルシシスト数です')
else:
    print(f'{number}はナルシシスト数ではありません')    