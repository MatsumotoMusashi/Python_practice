A = int(input('登録したい英単語数->'))
b = []
for c in range(A):
    d = (str(input('英単語->')), str(input('英単語の日本語訳->')))
    b.append(d)
dictionary = dict(b)
print('次の単語が登録されている->', dictionary)
for f in str(input('登録された英単語のみで構成された肯定の英文を入力->')).split(' '):
        print(dictionary[f])




