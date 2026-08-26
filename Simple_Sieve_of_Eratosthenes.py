from openpyxl import load_workbook
file = load_workbook('prime_number_discovery.xlsx')
shete = file.active
number = int(input('Range(2~):'))
alpha_1 = input('Alphabet:')
alpha_2 = input('Alphabet:')
shete[f'{alpha_1}1'] = 'n_th prime number'
shete[f'{alpha_2}1'] = 'prime number'
p = 3
i = 1
shete[f'{alpha_1}2'] = i
shete[f'{alpha_2}2'] = p - 1
#エラトステネスの篩
'''
自然数のうち小さい方から順に調べていく
調査対象の数pに対してprime_numberの中に入っている素数はpよりも小さい
例えばp=10のときprime_numberには2,3,5,7とp=10以前に見つかった素数が格納されている
それは小さい順に調べているので前の数は次に調べる数よりも必ず小さくなるためである
prime_numberにある素数でpを割っていくときpを割り切れなかった回数mがprime_numberの要素数と等しければ
p未満のすべての素数で割り切れないことになるのでpは素数となる
故にmとlen(prime_number)が等しい時pは素数でありprime_numberに追加される
pが合成数ならば素因数分解が可能でありp未満の素数で必ず1度は割り切れるので割り切れなかった回数mは
prime_numberの要素数(len(prime_number))よりも小さくなる
故にmとlen(prime_number)は等しくならないのでpは素数でなくprime_numberに追加されない
'''
prime_number = [(1, 2)]
while p <= number:
    m = 0
    for x, y in prime_number:
        if p%y != 0:
            m += 1
    if m == len(prime_number):
        i += 1
        prime_number.append((i, p))
    p += 1    
l = 2
for a, b in prime_number:
    shete[f'{alpha_1}{l}'] = a
    shete[f'{alpha_2}{l}'] = b
    l += 1
file.save('prime_number_discovery.xlsx')    