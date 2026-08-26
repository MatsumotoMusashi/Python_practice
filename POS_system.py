#POSシステム対象としたい商品の登録プログラム
a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
g = 0
h = 0
i = 0
j = 0
n = 0
alphabet = [a, b, c, d, e, f, g, h, i, j, n]
Number = int(input('登録したい商品数を入力' + (str(len(alphabet))) + '個以下->'))
k = 0
goods_list = []
goods_price = []
while k < Number:
    n = str(input('登録したい商品を入力->'))
    goods_list.append(n)
    goods_price.append((n, int(input('登録した商品の値段(円)を入力->'))))
    if k == Number - 1:
        print('登録した商品とその価格一覧↓')
        print(goods_price)
        Answer = str(input('最初からやり直したければ「はい」と、そうでなければ「いいえ」と入力->'))
        if Answer == 'はい':
            goods_list = []
            goods_price = []
            k = 0
            continue
    k += 1 
goods_price_dictionary = dict(goods_price)
goods_alphabet = []
for l in range(len(goods_list)):
    goods_tuple = (goods_list[l], alphabet[l])
    goods_alphabet.append(goods_tuple)
goods_POS = dict(goods_alphabet)    
#POSシステムのプログラム
while True:
    selection_number = int(input('いくつの商品を購入されましたか->'))
    customer_selection = []
#現実世界ではここで打ち込む商品名はバーコードに該当するのでは？
    for m in range(selection_number):
        customer_selection.append(str(input(str(m + 1) + '点目の商品名を入力->')))
    for goods in customer_selection:
        if goods in goods_list:
#下記の式で累算代入文を使うと何故かgoods_POS[goods]の中身が変数として認識されないため以下のように書いた
            goods_POS[goods] = goods_POS[goods] + 1
    insist = str(input('入力の繰り返しを終了するなら「はい」、そうでなければ「いいえ」を入力->'))
    if insist == 'はい':
        break        
#POSシステムの結果表示プログラム
#itemsメッソドを使わないと辞書はキーと値の組(タプル形式?)を取り出せない,辞書の変数じゃないと値の変化が保存されてない?
print('売り上げを表示します↓')
for commodity, point in goods_POS.items():
    print('「' + str(commodity) + '」の売れた個数は' + str(point) + '個で、'
           + '売り上げは' + str(int(goods_price_dictionary[commodity]) * int(point)) + '円です')