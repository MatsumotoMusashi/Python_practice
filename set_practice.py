a = {('User634', 'hippo89'), ('UssR1906', 'Stalyin49')}
b = (str(input('ユーザー名を入力してください->')), str(input('パスワードを入力してください->')))
c = b in a
if c == True:
    print('ログイン完了')
if c != True:
    print('ログインできません')
    