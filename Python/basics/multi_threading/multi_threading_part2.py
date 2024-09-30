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
# --> It will over come the inconsistency problem, then we can predict the output clearly.
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
# 1. Lock(): this will release Lock only one time.
# 2. RLock(): this will release Lock only two times.
# 3. Semaphore(): this will release the lock for all counts.
# 4. BoundedSemaphore(count): this will release the lock for particular counts only.

# 1. Lock():
# ==========
# from threading import *
# import time
# l = Lock()
# def wish(name):
#         l.acquire()
#         for i in range(1,6):
#                 print('Good Evening ',name)
#                 time.sleep(2)
#         l.release()
#         l.acquire()
# t1 = Thread(target=wish,args=('SAI',))
# t2 = Thread(target=wish,args=('NTR',))
# t1.start()
# t2.start()

# 1.1 Lock():
# ==========
# from threading import *
# l = Lock()
# l.acquire()
# print('Main Thread trying to execute lock')
# l.acquire()
# print('Main Thread trying to execute lock')


# 2. RLock():
# ==========
# from threading import *
# l = RLock()
# def factorial(n):

#     l.acquire()

#     if n == 0:
#         result = 1
#     else:
#         result = n * factorial(n-1)
#     l.release()
#     return result

# def result_func(n):
#     print('The Factorial of ', n, factorial(n))

# t1 = Thread(target=result_func,args=(5,))
# t2 = Thread(target=result_func,args=(9,))

# t1.start()
# t2.start()


# 3. Semaphore(count): this will release the lock for all counts.
# ====================
# from threading import *
# import time
# s = Semaphore(3)
# def wish(name):
#     s.acquire()
#     for i in range(1,6):
#         print('Good Evening ',name)
#         time.sleep(2)
#     s.release()
# t1 = Thread(target=wish,args=('Hello',))
# t2 = Thread(target=wish,args=('Greet',))
# t3 = Thread(target=wish,args=('Thanks',))
# t1.start()
# t2.start()
# t3.start()


# 4. BoundedSemaphore(count): this will release the lock for particular counts only.
# ==========================
# from threading import *
# import time
# s = BoundedSemaphore(3)
# def wish(name):
#     s.acquire()
#     for j in range(1,6):
#         print('Good Evening ',name,j)
#         time.sleep(3)
#     s.release()
#     s.release()
#     s.release()
# t1 = Thread(target=wish,args=('SAI',))
# t2 = Thread(target=wish,args=('NTR',))
# t3 = Thread(target=wish,args=('SURAJ',))
# t4 = Thread(target=wish,args=('Alice',))
# t5 = Thread(target=wish,args=('Bob',))
# t6 = Thread(target=wish,args=('John',))
# t1.start()
# t2.start()
# t3.start()
# t4.start()
# t5.start()
# t6.start()


# Inter Thread Communication:
# ===========================
# 1. Event()
# 2. Condition()
# 3. Queue()
# methods in Inter Thread Communication:
# ------------------------------------
# 1. set()
# 2. clear()
# 3. isSet()
# 4. wait()
# 5. wait(seconds)

# Ex: Realtime Example for Inter Thread Communication?
import threading
import time
event = threading.Event()
def trafficpolice():
    while True:
        time.sleep(5)
        print('Traffic Police given GREEN Signal')
        event.set()
        time.sleep(10)
        print('Traffic Police giving RED Signal')
        event.clear()
def driver():
    num = 0
    while True:
        print('Driver waiting for GREEN Signal')
        event.wait()
        print('Traffic Signal is GREEN.. Vehicles can move')
        while event.isSet():
            num = num+1
            print('Vehicle No',num,'Crossing the Signal')
            time.sleep(2)
        print('Traffic Signal is RED... Drivers have to wait')
t1 = threading.Thread(target=trafficpolice)
t2 = threading.Thread(target=driver)
t1.start()
t2.start()