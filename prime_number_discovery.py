#素数数え上げプログラム(素数判定のアルゴリズムを使用)
number = int(input('いくつまでの範囲で素数を調べたいですか->')) 
prime_number = [a for a in range(1, number + 1) if len([z for z in (y for y in range(1, a + 1)) if a%z == 0]) == 2]
if len(prime_number) != 0:    
    print(f'{number}までで素数は{len(prime_number)}個ありそれらは以下の数です↓')
    prime = prime_number.copy()
    del prime_number[-1]
    for b in prime_number:
       print(b, end = ', ')
    print(prime[-1])    
else:
    print(f'{number}までで素数は存在しません')    