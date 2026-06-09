import threading
from threading import Thread
from time import sleep

def naturalNo():
    print(threading.current_thread().name, "Has Started")
    sleep(2)
    for x in range(10):
        print(x)
    print(threading.current_thread().name, "Has Ended")

t1 = Thread(target=naturalNo)
t2 = Thread(target=naturalNo)
t1.start()
t2.start()

