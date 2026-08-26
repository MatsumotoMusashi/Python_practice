from openpyxl import load_workbook
file = load_workbook('attendance_number.xlsx')
shete = file.active
alpha_1 = input('Alphabet:')
alpha_2 = input('Alphabet:')
shete[f'{alpha_1}1'] = '出席番号'
shete[f'{alpha_2}1'] = '生徒氏名'
l = 2
number = int(input('クラス内の生徒総数を入力->'))
student = sorted([str(input('氏名を平仮名で入力->')) for a in range(number)])
for x, y in enumerate(student, 1):
    shete[f'{alpha_1}{l}'] = x
    shete[f'{alpha_2}{l}'] = y
    l += 1
shete[f'{alpha_1}{l}'] = '生徒総数'
shete[f'{alpha_2}{l}'] = f'{number}名'
file.save('attendance_number.xlsx')