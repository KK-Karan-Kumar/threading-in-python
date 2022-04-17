from threading import Thread
from queue import Queue
import threading
from time import sleep

class Producer:
    def __init__(self) -> None:
        self.q = Queue()

    def produce(self):
        for i in range(1,6):
            print("Item Produced",i)
            self.q.put(i)
            sleep(2)

class Consumer:
    def __init__(self,prod) -> None:
        self.prod = prod

    def consume(self):
        for i in range(1,6):
            print("Item Received", self.prod.q.get(i))

p = Producer()
c = Consumer(p)

t1 = Thread(target=p.produce)
t2 = Thread(target=c.consume)
t1.start()
t2.start()