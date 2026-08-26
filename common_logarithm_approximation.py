#常用対数の近似値を求めるプログラム
number = int(input('何の自然数の常用対数の近似値を求めたいですか->'))
digit = int(input('小数何桁まで求めたいですか->'))
'''
自身のコンピューターでは5桁以下の自然数の常用対数の近似値最大小数点以下3桁まで求められ現段階ではその範囲で
確実に正確な近似値を得られる。range(number**(10**digit))とすれば確実に正確になるがメモリ上の問題で処理が
不可能になるためrange(10**(digit + 1))としている。コンピューターのキャパシティーに応じて(digit + n)のn
の値を変え正確性を期すように。(コンピューターのキャパシティーが(限りなく)無限ならば
range(number**(10**digit))としたい。
'''
print(f'{number}の常用対数を小数第{digit}桁まで求めた結果を以下に示します↓')
if number == 1:
    print('log1 = ', format(float(0), f'.{digit}f'))
#index_numberは例えばlog2を求める過程での10^3<2^10<10^4の3に該当する数である。
else:
    index_number = max((a for a in range(10**(digit + 1)) if 10**a < number**(10**digit)))
    print(f'log{number} = ', format(index_number / (10**digit), f'.{digit}f'))