'''
全ての自然数において自然数の数字和はその自然数以下である。
フィボナッチ数a_3の数字和はa_3以下であり、またFibにはa_3以下のフィボナッチ数がすべて保存されている。
故にa_3の数字和がフィボナッチ数ならばa_3の数字和はa_3以下のフィボナッチ数ということになりリストFibに
含まれているのでelif sum([int(b) for b in str(a_3)]) in Fib:はTrueとなる。
上記の条件がTrueになったのならばa_3の数字和はa_3以下のフィボナッチ数であると判定できたので数字和が
フィボナッチ数のフィボナッチ数を格納するリストwantに追加する。
'''
number = int(input('いくつまで調べたいか->'))
a_1 = 1
a_2 = 1
Fib = [1]
want = [1]
while True:
    a_3 = a_2 + a_1
    Fib.append(a_3)
    if number < a_3:
        break
    elif sum([int(b) for b in str(a_3)]) in Fib:
        want.append(a_3)
    a_1 = a_2
    a_2 = a_3
if len(want) != 0:
    print(f'{number}までの範囲で数字和がフィボナッチ数であるフィボナッチ数は{len(want)}個存在しそれらは以下の数である↓')
    c = want.pop(-1)
    for d in want:
        print(d, end = ', ')
    print(c)
else:
    print(f'{number}までの範囲で数字和がフィボナッチ数のフィボナッチ数は存在しない')    