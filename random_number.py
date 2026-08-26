digit = int(input('何桁(1桁以上)の乱数を生成したいですか->'))
g = [e for e in str(digit)]    
amount = int(input('いくつの乱数を生成したいですか'))
key = int(input(f'0~9までの数を用いた{digit}桁の数を入力->'))
number = []
'''
xに代入された数における0を0出ない数に置き換えるためにまずxの各桁中に含まれる0の数を調べる
その後x中の0をすべて取り除くためにx中に存在する0の個数回分(b.count('0'))0をremoveメソッド
を使うことで取り除きその後取り除いた回数分(b.count('0'))0でない数(g[0])を追加する
この操作を行うことによってx中の0をすべて排除し排除された0の個数分0でない数で置き換えるため
結果としてx中の0を0出ない数に置き換えたことになる
但し排除された0と同じ位置に0でない数が追加されるわけではなく0を排除したxの末尾から0出ない数が
足されていくことに注意
この点は排除された0と同じ位置に0でない数字を入れられるように改善を試みたいものだ
また桁数の小さい範囲では値の重複が少ない個数で発生するためある一定の小さい桁数に関しては循環を発生
させる数を発生させない数に置き換えて重複を避けるなどの工夫も施したいものだ
'''
for a in range(amount):
    if digit%2 == 0:
        if len(str(key**2))%2 == 0:
            x = str(key**2)[int(len(str(key**2))/2) - int(digit/2):int(len(str(key**2))/2) + int(digit/2)]
            b = [y for y in x]
            c = b.count('0')
            if c != 0:
                for nu in range(c):
                    b.remove('0')
                for d in range(c):
                    b.append(g[0])
                x = ''.join(b)
            number.append(int(x))
            key = int(x) 
        else:
            x = str(key**2)[int(len(str(key**2))/2) - int(digit/2):int(len(str(key**2))/2)] + str(key**2)[int(len(str(key**2))/2) + 1:int(len(str(key**2))/2) + int(digit/2) + 1]
            b = [y for y in x]
            c = b.count('0')
            if c != 0:
                for nu in range(c):
                    b.remove('0')
                for d in range(c):
                    b.append(g[0])
                x = ''.join(b)
            number.append(int(x))
            key = int(x)               
    else:
        if len(str(key**2))%2 != 0:
            x = str(key**2)[int(len(str(key**2))/2) - int(digit/2):int(len(str(key**2))/2) + int(digit/2) + 1]
            b = [y for y in x]
            c = b.count('0')
            if c != 0:
                for nu in range(c):
                    b.remove('0')
                for d in range(c):
                    b.append(g[0])
                x = ''.join(b)
            number.append(int(x))
            key = int(x)
        else:
            x = str(key**2)[int(len(str(key**2))/2) - int(digit/2) - 1:int(len(str(key**2))/2)] + str(key**2)[int(len(str(key**2))/2) + 1:int(len(str(key**2))/2) + int(digit/2) + 1]     
            b = [y for y in x]
            c = b.count('0')
            if c != 0:
                for nu in range(c):
                    b.remove('0')
                for d in range(c):
                    b.append(g[0])
                x = ''.join(b)
            number.append(int(x))
            key = int(x)
for z in number:
    print(z)            