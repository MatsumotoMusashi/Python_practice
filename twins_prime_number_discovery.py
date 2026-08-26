#エラトステネスの篩
Number = int(input('自然数を入力->'))
prime_number = []
eliminate_number = []
for a in range(2, Number + 1):
    if a not in eliminate_number:
        prime_number.append(a)
        for b in range(2, Number + 1):
            if b%a == 0:
                eliminate_number.append(b)
#双子素数探索プログラム
twins_prime_number = []
for c in prime_number:
    if c + 2 in prime_number:
        twins_prime_number.append((c, c+2))
print(f'{Number}までの範囲にある双子素数は{len(twins_prime_number)}組ありそれらは以下の数です↓')
copy = twins_prime_number.copy()
del twins_prime_number[-1]
for d, e in twins_prime_number:
    print(f'({d}, {e}), ', end = '')
print(copy[-1])
