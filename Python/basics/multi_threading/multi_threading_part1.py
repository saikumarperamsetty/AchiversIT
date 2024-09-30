# Multi Threading:
# ===============
# multitasking:  Executing multiple tasks at a time is called "Multitasking". 
# 1. Processed Based: each task is a seperate independent process.
# 2. Thread Based: each task is a separate independent part of the same memory.

# How to Check Which Thread is Executing in Background in Python?
import threading
print('Current Executing Thread is: ', threading.current_thread().name)


# How to many ways to Create a Thread in Python?
# Ex1: Create Thread using without class?
# =======================================
from threading import Thread
def display():
    for i in range(1,6):
        print('Child Tread ',i)
t = Thread(target=display)
t.start()
for j in range(1,6):
    print('Main Thread ',j)


# Ex: Create Thread using with class?
# ==================================
from threading import Thread
class MyThread(Thread):
    def run(self):
        for i in range(1,6):
            print('Child Thread ',i)
t = MyThread()
t.start()
for j in range(1,6):
    print('Main Thread ',j)


# Ex:2 How to Squares and Double the numbers using with and without Thread class?
# without Threading Concept:
# =========================
import time
numbers = [1,2,3,4,5]
def double_numbers(numbers):
    for n in numbers:
        print('Duble Nums = ', 2*n)
def square_numbers(numbers):
    for n in numbers:
        print('Square Nums = ', n*n)

begin_time = time.time()
double_numbers(numbers)
square_numbers(numbers)
end_time = time.time()
print(f'Time taken: {end_time-begin_time}')

# with Threading Concept:
# ======================
import threading
import time
numbers = [1,2,3,4,5]
def double_numbers(numbers):
    for n in numbers:
        print('Duble Nums = ', 2*n)
def square_numbers(numbers):
    for n in numbers:
        print('Square Nums = ', n*n)

begin_time = time.time()
threading1 = threading.Thread(target=double_numbers,args=(numbers,))
threading2 = threading.Thread(target=square_numbers,args=(numbers,))
threading1.start()
threading2.start()
threading1.join()
threading2.join()
end_time = time.time()
print(f'Time taken: {end_time-begin_time}')


# Ex:3 Setting and Getting Name of Thread?
# ===================================
# Getting Name of Thread:
# -----------------------
import threading
print('Getting Name of Thread:',threading.current_thread().name)

# Setting Name of Thread:
# -----------------------
import threading
threading.current_thread().name = 'New Thread Name'
print('Setting Name of Thread:',threading.current_thread().name)


# Ex:4 How to Find Current and Main Thread Identification Number?
# ===============================================================
import threading
def child_thread_func():
    print('Child Thread Identification Number: ',threading.current_thread().ident)

if __name__ == '__main__':
    print('Main Thread Identification Number: ',threading.current_thread().ident)
    child_thread_obj = threading.Thread(target=child_thread_func)
    child_thread_obj.start()


# Ex:5 How to Find how many Threads are active?
# =============================================
from threading import Thread, current_thread, active_count
import time
def thread_active():
    print(current_thread().name),'..started'
    time.sleep(3)
    print(current_thread().name),'..ended'
if __name__ == '__main__':
    print('Main Thread Started')
    print('The Number of Active Threads:',active_count())

    t1 = Thread(target=thread_active,name='Child_Thread1')
    t2 = Thread(target=thread_active,name='Child_Thread2')
    t3 = Thread(target=thread_active,name='Child_Thread3')
    t1.start()
    t2.start()
    t3.start()
    print('The no of active Threads after thread Creation:',active_count())
    time.sleep(5)
    print('The no of active Threads after waiting::',active_count())
    print('Main Thread Ended..')


# Ex:6 How to Find wether the Thread is alive or not?
# ===================================================
from threading import Thread, current_thread
import time
def thread_alive_or_not():
    print(current_thread().name),'started'
    time.sleep(3)
    print(current_thread().name),'ended'

t1 = Thread(target=thread_alive_or_not,name='Child_Thread1')
t2 = Thread(target=thread_alive_or_not,name='Child_Thread2')

t1.start()
t2.start()

print(t1.name,"is Alive",t1.is_alive())
print(t2.name,"is Alive",t2.is_alive())

time.sleep(5)

print(t1.name,"is Alive",t1.is_alive())
print(t2.name,"is Alive",t2.is_alive())


# join() method:
# ==============
# --> if a Thread wants to wait untill completing the some other Thread.

# Ex:7 Working of join() method in Multithreading?
# ================================================
from threading import Thread
import time
def working_of_join_method():
    for i in range(1,6):
        print('Start Thread: ',i)
        time.sleep(1)
t1 = Thread(target=working_of_join_method)
t1.start()

t1.join(10)
for j in range(1,6):
    print('Join Thread: ',j)