import threading
from threading import Thread

class MyThread:
    def naturalNo(self):
        #if threading.current_thread().name == "Thread-1":
            for x in range(10):
                print(x)
        #else:
            #print("Hey this is not  Thread -1")

myObj = MyThread()
t = Thread(target=myObj.naturalNo)
t.start()

