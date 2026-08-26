number = int(input('グレゴリー・ライプニッツ級数の第何項まで調べたいですか->'))
i = 1
sum = 0
while i <= number:
    sum += (1/((2*i) - 1))*((-1)**(i - 1))
    i += 1
print(f'グレゴリー・ライプニッツ級数の第{number}項までより得られた円周率の近似値は以下の値である↓')
print(f'π = {4*sum}')