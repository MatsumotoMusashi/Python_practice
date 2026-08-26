i = 0
print('算数の試験を行います。問題は全部で3問です。頑張りましょう。')
print('問 次の式を計算しなさい')
print('1. 120+230+370')
a = int(input('答え>>'))
if a == 720:
    print('正解')
    i = i + 1
if a != 720:
    print('不正解')
    print('正解は720です')
print('2. 140-50')
b = int(input('答え>>'))
if b == 90:
    print('正解')
    i = i + 1
if b != 90:
    print('不正解')
    print('正解は90です')
print('3. 1000-289')
c = int(input('答え>>'))
if c == 711:
    print('正解')
    i = i + 1
if c != 711:
    print('不正解')
    print('正解は711です')
print('以上で算数の試験を終了します')
j = str(i)
print('あなたの得点>>' + j + '点')
if i == 3:
    print('素晴らしい')
if i == 2:
    print('なかなかなのではないでしょうか')
if i == 1:
    print('頑張りましょう')
if i == 0:
    print('何も言えません')



