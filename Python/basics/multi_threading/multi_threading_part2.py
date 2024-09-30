# Multi Threading part-2:
# What is Daemon Treads?
# Ans: Thre treads which are running in the background is called Deamon Thread.

# Ex:1 How to check current Thread is Daemon Thread or not?
import threading
print(threading.current_thread().isDaemon())    # output = False
print(threading.current_thread().daemon)        # output = False