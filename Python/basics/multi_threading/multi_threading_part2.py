# Multi Threading part-2:
# ======================
# --> Main Thread is always non Daemon Thread only.

# What is Daemon Treads:
# ======================
# Ans: Thre treads which are running in the background is called Deamon Thread.
# ---

# Ex:1 How to check current Thread is Daemon Thread or not?
# =========================================================
# import threading
# Approach-1
# print(threading.current_thread().isDaemon())    # output = False    (it will Check the Current Thread is Daemon or Not)

# Approach-2
# print(threading.current_thread().daemon)        # output = False    (it will Check the Current Thread is Daemon or Not)


# Ex:2 How to set Daemon Nature for current Thread or any other Thread?
# =====================================================================
# from threading import Thread
# t = Thread(target=lambda:None)
# t.setDaemon(True)                   # it will set thread behaviour is Daemon now
# print(t.isDaemon())                 # output = True


# Ex:3 How to check Daemon Nature and Non Daemon Nature of current Executing Thread or any other Thread?
# ======================================================================================================
# from threading import *
# import time
# def check_daemon_behaviour():
#     for i in range(1,6):
#         print('child thread: ',i)
#         time.sleep(1)
# t = Thread(target=check_daemon_behaviour)
# t.setDaemon(True)

# t.start()
# time.sleep(5)

# for j in range(1,6):
#     print('main thread: ',j)
# print('end of main thread')


# Synchronization in Multithreading:
# ==================================
# from threading import *
# import time
# def wish(name):
#     for i in range(1,6):
#         print('Good Evening ',name)
#         time.sleep(2)
# t1 = Thread(target=wish,args=('SAI',))
# t2 = Thread(target=wish,args=('NTR',))
# t1.start()
# t2.start()


# Synchronixation Methods:
# ========================
1. Lock(): this will release Lock only one time.
2. RLock(): this will release Lock only two times.
3. Semaphore(): 

# 1. Lock():
# ==========
from threading import *
import time
l = Lock()
def wish(name):
        l.acquire()
        for i in range(1,6):
                print('Good Evening ',name)
                time.sleep(2)
        l.release()
        l.acquire()
t1 = Thread(target=wish,args=('SAI',))
t2 = Thread(target=wish,args=('NTR',))
t1.start()
t2.start()

# 1.1 Lock():
# ==========
from threading import *
l = Lock()
l.acquire()
print('Main Thread trying to execute lock')
l.acquire()
print('Main Thread trying to execute lock')