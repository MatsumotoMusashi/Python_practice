def prime(x):
    """関数に渡された引数が素数かどうかを判定するプログラムです"""
    x = int(x)
    if len([z for z in (y for y in range(1, x + 1)) if x%z == 0]) == 2:
        print(f'{x}は素数です')
    else:
        print(f'{x}は素数ではありません')


prime((input('自然数を入力->')))