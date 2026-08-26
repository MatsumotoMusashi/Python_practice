a = str(input('文章を書いてください->'))
sentence = a.split('。')
print('あなたの書いた文章は' + str(len(sentence)- 1) + '文で構成されています。')