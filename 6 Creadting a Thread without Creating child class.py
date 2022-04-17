from threading import Thread

class MyThread:
    def show(self,a):
        for i in range(a):
            print(i)

mythread = MyThread()
thread1 = Thread(target=mythread.show,args=(10,)) 
thread1.start()