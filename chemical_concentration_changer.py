M = float(input('溶液の溶質の分子量を入力(半角)->'))
d = float(input('溶液の密度(g/ml)を入力(半角)->'))
Answer = str(input('溶液について「モル濃度」,「重量モル濃度」,「質量％濃度」のどれが求まっていますか->'))
C = float(input('求まっている濃度を入力->'))
if Answer == 'モル濃度':
    mass_concentration = (C*M) / (10*d)
    weight_molarity = (1000*C) / (1000*d - C*M)
    print('質量%濃度:', mass_concentration)
    print('重量モル濃度:', weight_molarity)
if Answer == '質量%濃度':
    N = C
    molarity = (10*N*d) / M
    weight_molarity = (1000*molarity) / (1000*d - molarity*M)
    print('モル濃度:', molarity)
    print('重量モル濃度:', weight_molarity)
if Answer == '重量モル濃度':
    L = C
    molarity = (1000*L*d) / (1000 + L*M)
    mass_concentration = (molarity*M) / (10*d)
    print('モル濃度:', molarity)
    print('質量%濃度:', mass_concentration)
