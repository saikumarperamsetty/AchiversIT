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


# queue module methods:
# =====================
# 1. LIFO(LastInFirstOut)
# 2. FIFO(FirstInLastOut)
# 3. Priority()

# 1. LIFO(LastInFirstOut)
# =======================
# 1.1 Queue():
# ===========
# import queue
# q = queue.Queue()
# q.put(15)
# q.put(5)
# q.put(20)
# q.put(10)
# while not q.empty():
#     print(q.get())

# 1.2 LifoQueue():
# ===============
# import queue
# q = queue.LifoQueue()
# q.put(15)
# q.put(5)
# q.put(20)
# q.put(10)
# while not q.empty():
#     print(q.get())

# 1.2 PriorityQueue():
# ===================
# import queue
# q = queue.PriorityQueue()
# q.put((15,'SAI'))
# q.put((5,'NTR'))
# q.put((20,'SURAJ'))
# q.put((10,'PYTHON'))
# while not q.empty():
#     print(q.get())



# Usage of Locks?
# ===============
# Excepition Handling in Threads:
# ===============================
# without Lock: means try,except and finally blocks
# ============
# import threading
# import time
# lock = threading.Lock()
# def safe_thread_func(thread_id):
#     print(f'Thread {thread_id} attempting to acquire Lock')
#     lock.acquire()
#     try:
#         print(f'Thread {thread_id} has acquired the Lock..')
#         time.sleep(2)
#         if thread_id == 2:
#            raise Exception('An error occured in Thread-2')
#         print(f'Thread {thread_id} has completed work')
#     except Exception as e:
#         print(f'Exception in Thread {thread_id}: {e}')
#     finally:
#         print(f'Thread {thread_id} is releasing the Lock')
#     lock.release()

# threads = []
# for i in range(1,4):
#     t = threading.Thread(target=safe_thread_func,args=(i,))
#     threads.append(t)
#     t.start()

# for t in threads:
#     t.join()
# print('All threads have finished')



# with Lock:
# ==========
import threading
import time
lock = threading.Lock()
def safe_thread_func(thread_id):
    print(f'Thread {thread_id} attempting to acquire Lock')
    with lock:
        print(f'Thread {thread_id} has acquired the Lock..')
        time.sleep(2)
        if thread_id == 2:
           raise Exception('An error occured in Thread-2')
        print(f'Thread {thread_id} has completed work')

threads = []
for i in range(1,4):
    t = threading.Thread(target=safe_thread_func,args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()