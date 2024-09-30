# Inter Thread Communication:
# ===========================
# 1. Event()
# 2. Condition()
# 3. Queue()

# 2. Condition():
# ===============
# methods are:
# ------------
# acquire()
# release()
# notify()
# notifyAll()
# wait()    --> wait until notification
# wait(seconds) --> wait until notification or get expired

# Ex: Condition() method in Inter Thread Communication?
# ====================================================
# import threading
# import time
# import random
# items = []
# c = threading.Condition()
# def producer(c):
#     while True:
#         c.acquire()
#         item = random.randint(1,101)
#         print('Producer producing the item',item)
#         items.append(item)
#         print('Producer giving the Notification')
#         c.notify()
#         c.release()
#         time.sleep(3)
# def consumer(c):
#     while True:
#         c.acquire()
#         print('Consumer waiting for updation')
#         c.wait()
#         print('Consumer consume the item',items.pop())
#         c.release()
#         time.sleep(3)
# t1 = threading.Thread(target=producer,args=(c,))
# t2 = threading.Thread(target=consumer,args=(c,))
# t1.start()
# t2.start()


# 3. Queue():
# ===========
# methods are:
# ------------
# put(): put an item into the queue
# get(): get an item into the queue

# Ex: Queue() method in Inter Thread Communication?
# =================================================
# import threading
# import time
# import random
# import queue
# q = queue.Queue()
# def producer(q):
#     while True:
#         item = random.randint(1,101)
#         print('Producer producing the item',item)
#         q.put(item)
#         print('Producer giving Notification')
#         time.sleep(3)
# def consumer(q):
#     while True:
#         print('Consumer waiting for Updation')
#         print('Consumer consumed the item',q.get())
#         time.sleep(3)
# t1 = threading.Thread(target=producer,args=(q,))
# t2 = threading.Thread(target=consumer,args=(q,))
# t1.start()
# t2.start()


queue module methods:
=====================
1. LIFO(LastInFirstOut)
2. FIFO(FirstInLastOut)
3. Priority()

1. LIFO(LastInFirstOut)
=======================
1.1 Queue():
===========
import queue
q = queue.Queue()
q.put(15)
q.put(5)
q.put(20)
q.put(10)
while not q.empty():
    print(q.get())

1.2 LifoQueue():
===============
import queue
q = queue.LifoQueue()
q.put(15)
q.put(5)
q.put(20)
q.put(10)
while not q.empty():
    print(q.get())

1.2 PriorityQueue():
===================
import queue
q = queue.PriorityQueue()
q.put((15,'SAI'))
q.put((5,'NTR'))
q.put((20,'SURAJ'))
q.put((10,'PYTHON'))
while not q.empty():
    print(q.get())