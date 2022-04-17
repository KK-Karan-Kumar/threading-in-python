from threading import Thread

#without parameter
def show():
    print("Threading is now running")

thread1 = Thread(target=show)

thread1.start()


#with parameter
def show2(num):
    for i in range(num):
        print(i)

thread2 = Thread(target=show2,args=(10,))
thread2.start()

#main thread

# for i in range(10):
    # print("m {}".format(i))