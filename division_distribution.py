from openpyxl import Workbook, load_workbook
div = load_workbook('division.xisx')
shete = div.active
alphabet_1 = input('Alphabet:')
alphabet_2 = input('Alphabet:')
shete[f'{alphabet_1}1'] = '自然数'
shete[f'{alphabet_2}1'] = '約数の個数'
l = 2
number = int(input('いくつまでの範囲の調査としたいですか'))
for a in range(1, number + 1):
    shete[f'{alphabet_1}{l}'] = a
    shete[f'{alphabet_2}{l}'] = len([b for b in range(1, a + 1) if a%b == 0])
    l += 1
div.save('division.xlsx')