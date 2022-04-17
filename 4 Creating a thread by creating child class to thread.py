from threading import Thread, main_thread

class MyThread(Thread):
    def run(self):
        for i in range(5):
            print("Child Thread")


thread1 = MyThread()
thread1.start()

for i in range(5):
    print("Main Thread")