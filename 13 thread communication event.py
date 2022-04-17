from threading import Thread,Event

from time import sleep

def light_switch():
    sleep(2)
    e.set()
    print("Green Light ON")
    sleep(4)
    print("Red Light ON")
    e.clear()
    
def traffic():
    e.wait()
    while e.is_set():
        print("You can go....")
        sleep(0.5)

    print("programe Done")

e = Event()

t1 = Thread(target=light_switch)
t2 = Thread(target=traffic)
t1.start()
t2.start()
