from openpyxl import load_workbook
pnd = load_workbook('prime_number_desert.xlsx')
shete = pnd.active
al_1 = input('Alphabet:')
al_2 = input('Alphabet:')
shete[f'{al_1}1'] = '素数'
shete[f'{al_2}1'] = '素数砂漠の長さ'
l = 2
number = int(input('いくつまでの範囲で素数を調べたいですか->')) 
prime_number = [a for a in range(1, number + 1) if len([z for z in (y for y in range(1, a + 1)) if a%z == 0]) == 2]
first = prime_number[0]
del prime_number[0]
for x in prime_number:
    shete[f'{al_1}{l}'] = f'{first}～{x}'
    shete[f'{al_2}{l}'] = x - first -1
    first = x
    l += 1
pnd.save('prime_number_desert.xlsx')    