from openpyxl import Workbook, load_workbook
bution = load_workbook('marcos_distribution.xlsx')
marcos = bution.active
alphabet_1 = input('Alphabet:')
alphabet_2 = input('Alphabet:')
alphabet_3 = input('Alphabet:')
marcos[f'{alphabet_1}1'] = '年'
marcos[f'{alphabet_2}1'] = '都市A'
marcos[f'{alphabet_3}1'] = '都市B' 
a = int(input('都市A->Bへの人口推移の％=>'))
b = int(input('都市B->Aへの人口推移の％=>'))
c = int(input('1年目の都市Aの全体に占める人口の割合％->'))
d = int(input('1年目の都市Bの全体に占める人口の割合％->'))
e, f, G, H = c/100, d/100, a/100, b/100
J, K = (100 - a)/100, (100 - b)/100
l = 1
marcos[f'{alphabet_1}2'] = 1
marcos[f'{alphabet_2}2'] = c
marcos[f'{alphabet_3}2'] = d
M = int(input('何年後までの分布を調べる？-->'))
num = 3
while l <= M:
    x = J*e + H*f
    y = G*e + K*f
    marcos[f'{alphabet_1}{num}'] = l + 1
    marcos[f'{alphabet_2}{num}'] = (x*100)
    marcos[f'{alphabet_3}{num}'] = (y*100)
    l += 1
    e = x
    f = y
    num += 1
bution.save('marcos_distribution.xlsx')