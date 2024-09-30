# Multi Threading part-2:
# ======================
--> Main Thread is always non Daemon Thread only.

# What is Daemon Treads:
# ======================
Ans: Thre treads which are running in the background is called Deamon Thread.
# ---

# Ex:1 How to check current Thread is Daemon Thread or not?
# =========================================================
import threading
# Approach-1
print(threading.current_thread().isDaemon())    # output = False    (it will Check the Current Thread is Daemon or Not)

# Approach-2
print(threading.current_thread().daemon)        # output = False    (it will Check the Current Thread is Daemon or Not)


# Ex:2 How to set Daemon Nature for current Thread or any other Thread?
# =====================================================================
from threading import Thread
t = Thread(target=lambda:None)
t.setDaemon(True)                   # it will set thread behaviour is Daemon now
print(t.isDaemon())                 # output = True