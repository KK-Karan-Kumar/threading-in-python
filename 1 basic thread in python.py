import threading

current_thread= threading.current_thread().getName()
print("Current Thread : {}".format(current_thread))