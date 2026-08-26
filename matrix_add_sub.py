print('a×b行列A,Bの和A+B,差A-Bを求める')
a = int(input('a = '))
b = int(input('b = '))
print('行列Aについて')
matrix_1 = []
for c in range(1, a + 1):
    con = []
    for d in range(1, b + 1):
        con.append(int(input(f'{c}×{d}成分を入力->')))
    matrix_1.append(con)
print('行列Bについて')
matrix_2 = []
for e in range(1, a + 1):
    con = []
    for f in range(1, b + 1):
        con.append(int(input(f'{e}×{f}成分を入力->')))
    matrix_2.append(con)
matrix_add = []
matrix_sub = []
for g in range(a):
    con_1 = []
    con_2 = []
    for h in range(b):
        s_1 = 0
        s_2 = 0
        s_1 = (matrix_1[g])[h] + (matrix_2[g])[h]
        s_2 = (matrix_1[g])[h] - (matrix_2[g])[h]
        con_1.append(s_1)
        con_2.append(s_2)
    matrix_add.append(con_1)
    matrix_sub.append(con_2)
print('-'*119)    
print('A+Bの行列は以下のようになる')
i = max([max(j) for j in matrix_add])
for m in matrix_add:
    o = m.pop(-1)
    for n in m:
        print(n, end = ' '*int(1 + len(str(i)) - len(str(n))))
    print(o)
print('-'*119)     
print('A-Bの行列は以下のようになる')
k = max([max(l) for l in matrix_2])
for p in matrix_sub:
    q = p.pop(-1)
    for r in p:
        print(r, end = ' '*int(1 + len(str(k))-len(str(r))))
    print(q)