from threading import Thread, current_thread

def show():
    #geting thread name with getName function
    print("Child Thread {}".format(current_thread().getName()))
    #set thread name with setname function
    current_thread().setName("Work")
    print("Child Thread {}".format(current_thread().getName()))

thread1 = Thread(target=show)
thread2 = Thread(target=show)

thread1.start()
thread2.start()
print("Main thread {}".format(current_thread().getName()))


def show1():
    #geting thread name with getName function
    print("Child Thread {}".format(current_thread().name))
    #set thread name with setname function
    current_thread().name  = "work2"
    print("Child Thread {}".format(current_thread().name))

thread3  = Thread(target=show1)
thread3.start()
"""

def show3():
    pass

thread4 = Thread(target=show3)

print("thread 4",thread4.getName())
thread4.setName("done")
print("thread 4",thread4.getName())

print("thread 4",thread4.name)
thread4.name = "done2"
print("thread 4",thread4.name)

"""

