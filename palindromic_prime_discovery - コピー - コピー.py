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
#回文素数を発見、表示するプログラム
palindromic_prime = [c for c in prime_number if str(c) == str(c)[::-1]]
print(f'{Number}までの範囲で見つかった回文素数は{len(palindromic_prime)}個でそれらは以下の数です↓')
copy = palindromic_prime.copy()
del palindromic_prime[-1]
for d in palindromic_prime:
    print(f'{d}, ', end = '')
print(copy[-1])
