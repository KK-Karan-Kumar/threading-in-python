from threading import Thread, current_thread
def disp():
    print("Daemon Thread")

t1 = Thread(target=disp)
print(t1.isDaemon())


#remember status change before start, you can't change running thread status

# t1.start() #error

#creating daemon thread using setDaemon function
t1.setDaemon(True)
print(t1.isDaemon())


#creating daemon thread using setDaemon function
t2 = Thread(target=disp)
print(t2.daemon)
t2.daemon = True
print(t2.daemon)

mt = current_thread()
print(mt.getName())
print("MT:",mt.isDaemon())

t3= Thread(target=disp)
print("T3:",t3.isDaemon())




from time import sleep

def teacher():
    for i in range(1,11):
        print("Teaching Session",i)
        sleep(1)

t1 = Thread(target=teacher)
t1.setDaemon(True)
t1.start()
sleep(6)
print("Exam Finished",current_thread().name)
