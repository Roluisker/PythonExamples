import threading
from threading import Thread

def even_odd():
    evenNo()
    print(threading.current_thread().name)
    oddNo()

def evenNo():
    print("Odd are")
    for x in range(10):
        if(x%2==0):
            print(x)

def oddNo():
    print("Odd No are")
    for x in range(10):
        if(x%2!=0):
            print(x)

t = Thread(target=even_odd, name="Event-Odd Thread")
t.start()