from threading import Thread
import os

path1 = input("请输入拷问地址：")
if path1[-1]!='/':
    path1+='/'
dirs=os.listdir(path1)

path2=input("请输入复制地址：")
if path2[-1]!='/':
    path2+='/'
os.mkdir(path2)

def copy_py(file):
    f = open(path1 + file,'rb')
    g = open(path2 + file, 'wb')
    while True:
        data=f.read(1024)
        if not data:
                break
        g.write(data)
    f.close()
    g.close()


jobs=[]
while True:
    for i in dirs:
        if not os.path.isfile(path1):
            path1=path1+i+'/'
            path2=path2+i+'/'
            dirs=os.listdir(path1)
            os.mkdir(path2)
        t=Thread(target=copy_py,kwargs={'file':i})
        jobs.append(t)
        t.start()

    for i in jobs:
        i.join()

    else:
        break