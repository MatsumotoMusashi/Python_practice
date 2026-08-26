#英文を数値に暗号化するプログラム
a = 'a/b/c/d/e/f/g/h/i/j/k/l/m/n/o/p/q/r/s/t/u/v/w/x/y/z/A/B/C/D/E/F/G/H/I/J/K/L/M/N/O/P/Q/R/S/T/U/V/W/X/Y/Z/./,/ '.split('/')
b = []
c = []
for d in range(len(a)):
    e = (str(a[d]), d)
    f = (d, str(a[d]))
    b.append(e)
    c.append(f)
code = dict(b)
reverse_code = dict(c)    
sentence = str(input('英文を入力->'))
sentence_list = []
for g in sentence:
    sentence_list.append(str(code[g]))
h = int(''.join(sentence_list))
i = {h: sentence_list}   
print('暗号化された英文を表示')
print(h)
#暗号化された文章を解読するプログラム
j = i[int(input('暗号化された英文を入力->'))]
translation = []
for m in j:
    translation.append(reverse_code[int(m)])
print('暗号化された文章を表示')
for n in translation:
    print(n, end = '') 

