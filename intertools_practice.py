from itertools import permutations, combinations
n = int(input('何桁の数を作りたいか->'))
want = []
for b in permutations([a for a in range(0, 10)], n):
    number = ''
    for c in b:
        number += str(c)
    want.append(int(number))
want.sort()
print(f'0~9を1回づつ用いた{n}桁の数は以下の数です↓')
d = want.pop(-1)
for e in want:
    if len(str(e)) == n:
        print(e, end = ', ')
if len(str(d)) == n:
    print(d)        