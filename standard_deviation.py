from math import sqrt
from fractions import Fraction
from openpyxl import load_workbook
file = load_workbook('data_gross.xlsx')
shete = file.active
alpha_1 = input('Alphabet:')
alpha_2 = input('Alphabet(data):')
l_1 = int(input('最初の行番号:'))
l_2 = int(input('最後の行番号:'))
digit = int(input('標準偏差を小数点以下何桁で求めたいか->'))
data = []
a = l_1
while a <= l_2:
    data.append(shete[f'{alpha_2}{a}'].value)
    a += 1        
b = Fraction(sum(data), len(data))
c = Fraction(0, 1)
for d in data:
    c += (Fraction(d, 1) - b)**2
shete[f'{alpha_1}{l_2 + 1}'] = '標準偏差'
shete[f'{alpha_2}{l_2 + 1}'] = format(sqrt((c/Fraction(len(data), 1))), f'.{digit}f')   
file.save('data_gross.xlsx')