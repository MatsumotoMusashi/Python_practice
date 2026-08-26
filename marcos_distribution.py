a = int(input('都市A->Bへの人口推移の％=>'))
b = int(input('都市B->Aへの人口推移の％=>'))
c = int(input('1年目の都市Aの全体に占める人口の割合％->'))
d = int(input('1年目の都市Bの全体に占める人口の割合％->'))
e, f, G, H = c/100, d/100, a/100, b/100
J, K = (100 - a)/100, (100 - b)/100
l = 1
M = int(input('何年後までの分布を調べる？-->'))
while l <= M:
    x = J*e + H*f
    y = G*e + K*f
    n = (x*100)
    l += 1
    print(str(l) + '年目の都市Aの全体に占める人口の割合->' + str(n) + '％')
    e = x
    f = y
l = 1
e, f = c/100, d/100
while l <= M:
    x = J*e + H*f
    y = G*e + K*f
    o = (y*100)
    l += 1
    print(str(l) + '年目の都市Bの全体に占める人口の割合->' + str(o) + '％')
    e = x
    f = y    