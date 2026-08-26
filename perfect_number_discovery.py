#完全数探索プログラム
number = int(input('いくつまでの範囲で完全数を調べたいですか->'))
perfect_number = [a for a in range(1, number + 1) if sum((b for b in range(1, a) if a%b == 0)) == a]    
if len(perfect_number) != 0:
    print(f'{number}までで完全数は{len(perfect_number)}個ありそれらは以下の数です↓')
    per = perfect_number[-1]
    del perfect_number[-1]
    for c in perfect_number:
        print(c, end = ', ')
    print(per)
else:
    print(f'{number}までで完全数は存在しません')           