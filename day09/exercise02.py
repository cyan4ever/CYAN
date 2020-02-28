from threading import Lock,Thread,Event

# lock1=Lock()
e1=Event()
# lock2=Lock()
e2=Event()

def print_num():
    for i in range(1,53,2):
        # lock1.acquire()
        e1.wait()
        print(i)
        print(i+1)
        # lock2.release()
        e2.set()


def print_char():
    for i in range(65,91):
        # lock2.acquire()
        e2.wait()
        print(chr(i))
        # lock1.release()
        e1.set()

t1=Thread(target=print_num)
t2=Thread(target=print_char)

# lock2.acquire()


t1.start()
t2.start()

e1.set()


t1.join()
t2.join()