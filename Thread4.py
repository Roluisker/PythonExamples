import threading
from threading import Thread

class MyThread(Thread):
    def run(self):
        print("Torre de cali")
        print(threading.current_thread().name)
        for x in range(0,5):
            for j in range(0,x+1):
                print("*", end=" ")


objMyThread = MyThread()
objMyThread.run() # tun() lo corre en el main thread
objMyThread.start() # lo corre en un nuevo hilo distinto al main trehard