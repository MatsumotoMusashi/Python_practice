'''
(x1, y1),(x2, y2),...(xn, yn)のn個のデータの近似曲線を導出するのに最小二乗法を用いるがこのとき
xのデータ数(len(x))とyのデータ数(len(y))はn個で共通している。
エクセルの指定範囲のデータについて上から順にx1,y1...,xn,ynとすると上から順にx,yのデータをリストx,yに
入れていったとき各リストには入れた順に入るからリストxは[x1, x2, x3,...,xn]、リストyは[y1, y2, y3,...,yn]
のように上から順にx,yのデータの組が各リストx,yに保存されている。(l.21~22)
よって共分散を取るときエクセルの同じ行にあるデータを取り出すので、リストでは同じインデックスのx,yのデータを
取り出すことになる。またx,yのデータ数も共通していることから0~len(x)の範囲でとってもlen(x)=len(y)である
ことから範囲外のインデックスとなってしまうことがない。
以上より共分散の(x1-ux)(y1-uy)+...+(xn-ux)(yn-uy)の部分はリストx,yを用いて(x[0]-ux)(y[0]-uy)+...
+(x[len(x)-1]-ux)(y[len(x)-1]-uy)と書くことができる。(l.25~29)
'''
from openpyxl import load_workbook
file = load_workbook(input('ファイル名を入力->') + '.xlsx')
shete = file.active
alpha_1 = input('Alphabet(x軸データ):')
alpha_2 = input('Alphabet(y軸データ):')
print('何行目から何行目までのデータに関して調べたいか->')
a = int(input('最初の行番号->'))
b = int(input('最後の行番号->'))
x = [float(shete[f'{alpha_1}{c}'].value) for c in range(a, b + 1)]
y = [float(shete[f'{alpha_2}{d}'].value) for d in range(a, b + 1)]
ux = sum(x)/len(x)
uy = sum(y)/len(y)
e = 0
g = 0
for f in range(len(x)):
    e += (x[f] - ux)**2
    g += (x[f] - ux)*(y[f] - uy)
s_x = e/len(x)
Cov = g/len(x)
A = Cov/s_x
B = uy - A*ux
print('-'*119)
print('2つのデータの最小二乗法より得られた近似直線の式は以下のようになる↓')
if B < 0:
    print(f'y={A}x{B}')
elif B == 0:
    print(f'y={A}x')
else:
    print(f'y={A}x+{B}')        