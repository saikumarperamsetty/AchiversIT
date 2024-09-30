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
# wait()
# wait(seconds)

# Ex: Condition() method in Inter Thread Communication?
# ====================================================
import threading
import time
import random
items = []
c = threading.Condition()
def producer(c):
    while True:
        c.acquire()
        item = random.randint(1,101)
        print('Producer producing the item',item)
        items.append(item)
        print('Producer giving the Notification')
        c.notify()
        c.release()
        time.sleep(3)
def consumer(c):
    while True:
        c.acquire()
        print('Consumer waiting for updation')
        c.wait()
        print('Consumer consume the item',items.pop())
        c.release()
        time.sleep(3)
t1 = threading.Thread(target=producer,args=(c,))
t2 = threading.Thread(target=consumer,args=(c,))
t1.start()
t2.start()