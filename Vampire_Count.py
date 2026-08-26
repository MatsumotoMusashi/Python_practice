from itertools import permutations
number_1 = int(input('初期値->'))
number_2 = int(input('最終値->'))
want = []
for a in range(number_1, number_2 + 1):
    s = 0
    if len(str(a))%2 == 0:
        n_list3 = [b for b in str(a)]
        for d, e in permutations([c for c in permutations(n_list3, int(len(str(a))/2))], 2):
            out = 0
            if d[-1] != 0 or e[-1] != 0:
                n_list1 = []
                n_list2 = []
                n_1 = ''
                n_2 = ''
                for f in d:
                    n_list1.append(f)
                    n_1 += f
                for g in e:
                    n_list2.append(g)
                    n_2 += g
                for h in str(a):
                    if n_list1.count(h) + n_list2.count(h) != n_list3.count(h):
                        out += 1
                if out == 0:    
                    if int(n_1)*int(n_2) == a:
                        s += 1
    if 1 <= s:
        want.append(a)        
if len(want) != 0:
    print(f'{number_1}~{number_2}までの範囲でヴァンパイア数は{len(want)}個存在しそれらは以下の数である↓')
    i = want.pop(-1)
    for j in want:
        print(j, end = ', ')
    print(i)
else:
    print(f'{number_1}~{number_2}の範囲でヴァンパイア数は存在しない')        