number_1 = int(input('初期値:'))
number_2 = int(input('最終値:'))
want = []
for a in range(number_1, number_2 + 1):
    if int(str(a**2)[-len(str(a)):]) == a:
        want.append(a)
if len(want) != 0:    
    print(f'{number_1}~{number_2}の範囲で自己同形数は{len(want)}個存在しそれらは以下の数である↓')
    b = want.pop(-1)
    for c in want:
        print(c, end = ', ')
    print(b)
else:
    print(f'{number_1}~{number_2}の範囲で自己同形数は存在しない')        