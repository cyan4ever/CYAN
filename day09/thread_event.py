"""
event线程同步互斥方法实例
"""

from threading import Event,Thread

s = None
e = Event

def yzr():
    print("杨子荣前来拜山头")
    global s
    s="天王盖地虎"
    e.set()

t = Thread(target=yzr)
t.start()

print("说对口令就是自己人")
e.wait()
if s =="天王盖地虎":
    print("宝塔镇河妖")
    print("确认过眼神，你是对的人")

else:
    print("打死你个龟孙")

t.join()