#暗号化-復号化keyの設定
x_1 = int(input('10桁の自然数を入力->'))
word = input('好きな英単語を入力->')
alphabet = [c for c in 'abcdefghijklmnopqrstuvwxyz.?- ']
Alpha= [b for b in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ,!']
a = set()
while len(a) < (len(alphabet) + len(Alpha)):
    x_2 = (48271*x_1)%(2147483647)
    a.add(x_2)
    x_1 = x_2
number = [e for e in a]
wo_nu = []
nu_wo = []
for d in range(len(alphabet)):
    wo_nu.append((alphabet[d], number[d]))
    nu_wo.append((number[d], alphabet[d]))
i = 0
j = len(alphabet)
while i < len(Alpha):
    wo_nu.append((Alpha[i], number[j]))
    nu_wo.append((number[j], Alpha[i]))
    i += 1
    j += 1
word_encoding = dict(wo_nu)
number_translation = dict(nu_wo)
while True:
    Answer = input('暗号化したければ「暗号化」、復号化したければ「復号化」と入力->') 
    #暗号化
    if Answer == '暗号化':
        sentence = input('英文を入力->')
        en = [str(word_encoding[x]) for x in sentence]
        print('暗号化した英文↓')
        print(f'{word}'.join(en))
    #復号化
    if Answer == '復号化':
        kazu = input('暗号文を入力->')
        print('復号化された英文↓')
        for k in [number_translation[int(z)] for z in kazu.split(f'{word}')]:
            print(k, end = '')
        print('')
    print('-'*119)   