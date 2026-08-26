a = 1
B = int(input('いくつの英単語を辞書に登録したいですか->'))
c = []
while a <= B:
    d = (str(input('英単語を入力してください->')), str(input('英単語の意味を入力してください->')))
    c.append(d)
    a += 1
dictionary = dict(c)    
print('次のように英単語が登録されました->', dictionary)
e = 1
time = int(input('いくつの英単語の意味を調べたいですか->'))
while e <= time:
    f = str(input('意味を調べたい英単語を入力してください->'))
    if f not in dictionary:
        print('その英単語は登録されていません。登録済みの英単語を検索してください。')
        continue
    g = str(dictionary[f])
    print(f + 'の意味->' + g)
    e += 1
