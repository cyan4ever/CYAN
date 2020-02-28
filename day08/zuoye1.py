from threading import Thread
import os

path1 = "../day04"
dirs=os.listdir(path1)

path2="../day09"
os.mkdir(path2)

def copy_py(file):
    f = open(path1+'/'+file,'rb')
    g = open(path2 + '/' + file, 'wb')
    while True:
        data=f.read(1024)
        if not data:
                break
        g.write(data)
    f.close()
    g.close()


jobs=[]
for i in dirs:
    if os.path.isfile():
        t=Thread(target=copy_py,kwargs={'file':i})
        jobs.append(t)
        t.start()

for i in jobs:
    i.join()



