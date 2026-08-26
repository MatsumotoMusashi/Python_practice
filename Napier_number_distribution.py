from openpyxl import load_workbook
file = load_workbook('Napier_number.xlsx')
shete = file.active
alpha_1 = input('Alphabet:')
alpha_2 = input('Alphabet:')
shete[f'{alpha_1}1'] = 'n'
shete[f'{alpha_2}1'] = 'ネイピア数'
number = int(input('いくつまでの範囲で調べたいですか->'))
l = 2
for n in range(1, number + 1):
    shete[f'{alpha_1}{l}'] = n
    shete[f'{alpha_2}{l}'] = (1 + (1/n))**n
    l += 1
file.save('Napier_number.xlsx')    