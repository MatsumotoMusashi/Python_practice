from openpyxl import load_workbook
file = load_workbook('arithmetic_geometric_mean.xlsx')
shete = file.active
alpha_1 = input('Alphabet:')
alpha_2 = input('Alphabet:')
number = int(input('第何項まで調べたいですか->'))
shete[f'{alpha_1}1'] = 'n'
shete[f'{alpha_2}1'] = '第n項'
a_1 = int(input('初項の自然数(2以上)を入力->'))
shete[f'{alpha_1}2'] = 1
shete[f'{alpha_2}2'] = a_1
l = 3
for x in range(2, number + 1):
    a_2 = (a_1 + (1/a_1))/2
    shete[f'{alpha_1}{l}'] = x
    shete[f'{alpha_2}{l}'] = a_2
    a_1 = a_2
    l += 1
file.save('arithmetic_geometric_mean.xlsx')