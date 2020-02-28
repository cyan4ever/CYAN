from multiprocessing import Process
from time import sleep


def worker(sec,name):
    for i in range(3):
        sleep(sec)
        print("I'm %s"%name)
        print("I'm working...")

if __name__=='__main__':
    p = Process(target=worker,args=(2,'lucy'))
    p.daemon=True
    p.start()
    print("Name:",p.name)
    print("is alive:",p.is_alive())
    print("PID:",p.pid)
    p.join()
