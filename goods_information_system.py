#intは全角数字を半角数字にする cf:１23 int-> 123
A = int(input('登録したい商品数->'))
b = []
c = []
d = []
for e in range(A): 
    number = str(int(input(str(e + 1) + 'つ目の登録したい商品番号->')))
    goods = str(input('商品名->'))
    price = str(int(input('商品価格を入力->')))
    madein = str(input('原産国を入力->'))
    b.append(tuple([number, goods]))
    c.append(tuple([number, price]))
    d.append(tuple([number, madein]))
number_goods = dict(b)
number_price = dict(c)
number_madein = dict(d)
G = int(input('何回商品情報の開示をしたいか->'))
h = 1
while h <= G:
    print('商品情報の開示を行います')
    j = str(int(input('登録した商品番号を入力->')))
    if j not in number_goods:
        print('その商品番号は未登録です。')
        k = str(input('操作をやり直したければ「はい」と入力してください。そうでなければ操作を終了します->'))
        if k != 'はい':
            break
        continue
    print('商品名->' + str(number_goods[j]), '価格->' + str(number_price[j]) + '円', '原産国->' + str(number_madein[j]))
    h += 1