from threading import Thread, current_thread

class MyThread(Thread):
    def __init__(self,a):
        Thread.__init__(self)
        print("Child Thread",a)

    def run(self):
        pass

thread1 = MyThread(10)
thread1.start()

print("Main Thread")