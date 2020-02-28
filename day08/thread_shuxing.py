from threading import Thread
from time import sleep

def fun():
    sleep(3)
    print("线程属性测试")

t =Thread(target=fun)
t.start()
t.setName()



t.setName("Tedu")
print("Name:"+t.getName())
print("is alive:", t.is_alive())