c = 0
while c != 'はい':
    drink = []
    a = 1
    B = int(input('何種類の飲料を登録したいですか？->'))
    while a <= B:
        drink.append(input('登録したい飲料名を1つ入力->'))
        a += 1
    print('このように飲料が登録されました->', drink)
    c = (input('終了してよろしければ「はい」とそうでなければ「いいえ」と入力して下さい->'))    