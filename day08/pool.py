"""
进程池演示
*父进程结束，进程池也会销毁
*执行的事件函数必须在
"""
from multiprocessing import Pool
from time import sleep,ctime

#进程池事件
def worker(msg):
    sleep(2)
    print(ctime(),'--',msg)

pool=Pool(4)

#向进程池里放事件
for i in range(10):
    msg = "Tedu%d"%i
    pool.apply_async(func=worker,args=(msg,))

pool.close()

pool.join()