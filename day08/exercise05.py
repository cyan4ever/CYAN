from multiprocessing import Process
import time

def timeit(f):
    def wrapper(*args,**kwargs):
        start_time=time.time()
        res=f(*args,**kwargs)
        end_time=time.time()
        print("函数执行时间：",end_time-start_time)
        return res
    return wrapper

def isPrime(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n % i==0:
            return False
    return True

@timeit
def no_process():
    prime=[]
    for i in range(1,1000001):
        if isPrime(i):
            prime.append(i)
    print(sum(prime))

class Prime(Process):
    def __init__(self, begin, end):
        super().__init__()
        self.begin=begin
        self.end=end

    def run(self):
        prime =[]
        for i in range(self.begin,self.end):
            if isPrime(i):
                prime.append(i)
        print(sum(prime))

@timeit
def process_4():
    jobs=[]
    for i in range(1,100001,10000):
        p=Prime(i,i+10000)
        jobs.append(p)
        p.start()

    for i in jobs:
        i.join()

process_4()