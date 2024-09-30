# Multi Threading:
# ===============
# multitasking:  Executing multiple tasks at a time is called "Multitasking". 
# 1. Processed Based: each task is a seperate independent process.
# 2. Thread Based: each task is a separate independent part of the same memory.

# How to Check Which Thread is Executing in Background in Python?
import threading
print('Current Executing Thread is: ', threading.current_thread().name)


# How to many ways to Create a Thread in Python?
# Ex: Create Thread using without class?
from threading import Thread
def display():
    for i in range(1,6):
        print('Child Tread ',i)
t = Thread(target=display)
t.start()
for j in range(1,6):
    print('Main Thread ',j)


# Ex: Create Thread using with class?
from threading import Thread
class MyThread(Thread):
    def run(self):
        for i in range(1,6):
            print('Child Thread ',i)
t = MyThread()
t.start()
for j in range(1,6):
    print('Main Thread ',j)