from threading import Thread
class MyTest:
    def solve_question(self):
        self.q1()
        self.q2()
        self.q3()
    def q1(self):
        print("Question 1 Solved")
    def q2(self):
        print("Question 2 Solved")
    def q3(self):
        print("Question 3 Solved")

mytest = MyTest()

thread1 = Thread(target=mytest.solve_question)
thread1.start()
