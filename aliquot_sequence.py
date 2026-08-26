'''
s_1の値が0になれば定義より数列生成の操作を終了とする。
s_1の値が前に出た値となる(elif s_1 in seq)なら繰り返しに突入したことになる(a→...→b→...→a)ため繰り返し
だと断定できるので操作を終了する。
操作を終了するときs_1の値は繰り返し部分の最初の値になる。(e = s_1)
繰り返しに入ったらseqに値を追加する操作も終了するためseqの最後に追加された値は繰り返しに入る直前の値と
なる。(→a→...→b→...→c→...→d→b→...→c→...→d→b→...→c)
上記の図より繰り返し箇所は(b→...→c→...→d)となりseqのリストでは(→a→...→b→...→c→...→d)まで保存されている。
本プログラムではe=s_1=bとなっているためseq[seq.index(e):]で繰り返し箇所(b→...→c→...→d)の数列はスライス
できる。(l.39,l.46~49)
それ以外の場合はまだ数列が終了するとも繰り返しになるとも断定できていないため操作を続ける。
'''
number = int(input('最初の自然数を決定->'))
seq = [number]    
s_0 = number
while True:
    b = 1
    div = []
    while b <= s_0:
        if b in div:
            break
        if b**2 == s_0:
            div.append(b)
        elif s_0%b == 0:
            div.append(b)
            div.append(int(s_0/b))
        b += 1
    s_1 = sum(div) - s_0   
    if s_1 == 0:
        seq.append(s_1)
        break
    elif s_1 in seq:
        e = s_1
        break
    else:
        seq.append(s_1)
    s_0 = s_1
if seq[-1] != 0:
    if len(seq[(seq.index(e)):]) != len(seq):    
        print(f'{number}から始まるアリコット数列は以下のようになる↓')
        copy = seq.copy()
        c = seq.pop(-1)
        for d in seq:
            print(d, end = '→')
        print(f'{c}...')
        if len(copy[copy.index(e):]) != 1:
            print(f'上記の数列の{(copy[copy.index(e):])[0]}~{(copy[copy.index(e):])[-1]}が周期{len(copy[copy.index(e):])}の繰り返しとなる')
        else:
            print(f'上記の数列の{e}が周期{len(copy[copy.index(e):])}の繰り返しとなる')    
    else:
        print(f'{number}から始まるアリコット数列は以下の数列の周期{len(seq)}の繰り返しとなる↓')
        c = seq.pop(-1)
        for d in seq:
            print(d, end = '→')
        print(c)        
else:
    print(f'{number}から始まるアリコット数列は以下のようになる↓')
    c = seq.pop(-1)
    for d in seq:
        print(d, end = '→')
    print(c)                    