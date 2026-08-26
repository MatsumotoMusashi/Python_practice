a = str(input('生徒氏名を入力->'))
b = int(input('生徒の受講科目数->'))
c = 0
d = []
while c < b:
    e = str(input('生徒の受講科目を入力->'))
    d.append(e)
    if c == b - 1:
        print('受講科目はこれで間違いありませんか->',d)
        f = str(input('間違いがなければ「いいえ」と、間違いがあれば「はい」と入力して最初からやり直してください->'))
        if f == 'はい':
            c = 0
            d = []
            continue
    c += 1    
g = 0
subject_score = []
subject_rep = []
score_list = []
while g < len(d):
    score = int(input(d[g] + 'の点数を入力->'))
    score_list.append(score)
    h = (d[g], score)
    subject_score.append(h)
    if score <= 40:
        rep = 'C'
    elif score <= 80:
        rep = 'B'
    else:
        rep = 'A'
    i = (d[g], rep)
    subject_rep.append(i)
    if g == len(d) - 1:
        print('各受講科目の点数はこれでよろしいですか->', subject_score)
        j = str(input('間違いがなければ「いいえ」と、間違いがあれば「はい」と入力して最初からやり直してください->'))
        if j == 'はい':
            g = 0
            subject_score = []
            subject_rep = []
            score_list = []
            continue
    g += 1
k = 0
sum = 0
while k < len(score_list):
    sum += score_list[k]
    k += 1
print('「' + a + '」' + 'の成績は以下のようになります。')
for l, m in subject_rep:
    print(l + ':' + m)
#40*bは100*b*0.4で全科目の点数100*bの40%であることを意味する。
if sum <= 40*b:
    print('「留年」')
else:
    print('「進級」')    