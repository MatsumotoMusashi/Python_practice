from glob import glob
from time import sleep
old = set(glob('*'))
while True:
    sleep(3)
    new = set(glob('*'))
    for x in new:
        if x not in old:
            print('append_file:', x)
    for y in old:
        if y not in new:
            print('del_file:', y) 
    old = new        