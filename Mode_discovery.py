from openpyxl import load_workbook
file = load_workbook('data_gross.xlsx')
shete = file.active
alpha_1 = input('Alphabet(data):')
alpha_2 = input('Alphabet:')
line_1 = int(input('最初の行番号:'))
line_2 = int(input('最後の行番号:'))
a = []
for b in range(line_1, line_2 + 1):
    a.append(shete[f'{alpha_1}{b}'].value)
b = set(x for x in a)
d = []
e = []
for c in b:
    d.append((c, a.count(c)))
    e.append(a.count(c))
shete[f'{alpha_2}{line_2 + 1}'] = '最頻値'
i = line_2 + 1
for h in [f for f, g in d if g == max(e)]:
    shete[f'{alpha_1}{i}'] = h
    i += 1
file.save('data_gross.xlsx')