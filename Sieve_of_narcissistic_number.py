#ナルシシスト数の列挙プログラム
narci_number = []
ra = int(input('いくつまでの範囲でナルシシスト数を調べたいですか->'))
narci_number = [a for a in range(1, ra + 1) if a == sum([int(x)**len(str(a)) for x in str(a)])]
if len(narci_number) != 0:
    print(f'{ra}まででナルシシスト数は{len(narci_number)}個ありそれらは以下の数です↓')
    narci = narci_number.copy()
    del narci_number[-1]
    for b in narci_number:
        print(b, end = ', ')
    print(narci[-1])
else:
    print(f'{ra}まででナルシシスト数はありませんでした')    