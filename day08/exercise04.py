from multiprocessing import Process

class MyProcess(Process):
    def __init__(self, value):
        super().__init__()
        self.value=value

    def fun1(self):
        print("步骤1")

    def fun2(self):
        print("步骤2")

    def run(self):
        self.fun1()
        self.fun2()

p = MyProcess(2)
p.start()
p.join()
        

