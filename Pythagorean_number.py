#1番目に大きい整数と2番目に大きい整数の差が1で一定のピタゴラス数の組を発見するプログラム
a = 1
Number = []
Pythagorean_number = []
sum = a
Answer = int(input('いくつのピタゴラス数の組を求めたいですか->'))
Times = 1
while Times <= Answer:
    b = a + 2
    sum += b
    a = b
    for c in range(0, b):
        if c**2 == b:
            Pythagorean_number.append(c)
            sum_pri = sum - b
            for d in range(0, sum_pri):
                if d**2 == sum_pri:
                    Pythagorean_number.append(d)
            for e in range(0, sum_pri + b):
                if e**2 == sum_pri + b:
                    Pythagorean_number.append(e)
            Number.append(Pythagorean_number)
            Pythagorean_number = []
            Times += 1
        else:
            continue
print(str(Answer) + '組のピタゴラス数↓')
for w in Number:
        print('(' + str(w[0]) + ', ' + str(w[1]) + ', ' + str(w[2]) + ')')
