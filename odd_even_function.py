#ネスト構造のプログラミングを作ろうcf:青という条件で複数の要素を抽出しさらにそれらの要素を値段で細分化していく検索モジュールもどきを作ろう
'''
int関数は文字列整数を整数型の整数にできるが文字列浮動小数点数を浮動小数点数型の数字に変換はできないので
float関数で一度浮動小数点数型の数字にしてからint関数に引数として渡して整数型の整数にする
float関数は文字列整数、浮動小数点数を一度に浮動小数点数型の数字に変換できる
'''
def odd_even(number):    
    if int(float(number)) != float(number):
        return 'error'
    elif int(float(number))//2 < int(float(number))/2:
        return 'odd'
    else:
        return 'even'

       
print(odd_even(input('number:')))