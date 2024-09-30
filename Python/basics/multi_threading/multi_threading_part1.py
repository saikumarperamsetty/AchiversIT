# Multi Threading:
# ===============
# multitasking:  Executing multiple tasks at a time is called "Multitasking". 
# 1. Processed Based: each task is a seperate independent process.
# 2. Thread Based: each task is a separate independent part of the same memory.

# How to Check Which Thread is Executing in Background in Python?
# import threading
# print('Current Executing Thread is: ', threading.current_thread().name)


# How to many ways to Create a Thread in Python?
# Ex1: Create Thread using without class?
# =======================================
# from threading import Thread
# def display():
#     for i in range(1,6):
#         print('Child Tread ',i)
# t = Thread(target=display)
# t.start()
# for j in range(1,6):
#     print('Main Thread ',j)


# Ex: Create Thread using with class?
# ==================================
# from threading import Thread
# class MyThread(Thread):
#     def run(self):
#         for i in range(1,6):
#             print('Child Thread ',i)
# t = MyThread()
# t.start()
# for j in range(1,6):
#     print('Main Thread ',j)


# Ex:2 How to Squares and Double the numbers using with and without Thread class?
# without Threading Concept:
# =========================
# import time
# numbers = [1,2,3,4,5]
# def double_numbers(numbers):
#     for n in numbers:
#         print('Duble Nums = ', 2*n)
# def square_numbers(numbers):
#     for n in numbers:
#         print('Square Nums = ', n*n)

# begin_time = time.time()
# double_numbers(numbers)
# square_numbers(numbers)
# end_time = time.time()
# print(f'Time taken: {end_time-begin_time}')

# with Threading Concept:
# ======================
# import threading
# import time
# numbers = [1,2,3,4,5]
# def double_numbers(numbers):
#     for n in numbers:
#         print('Duble Nums = ', 2*n)
# def square_numbers(numbers):
#     for n in numbers:
#         print('Square Nums = ', n*n)

# begin_time = time.time()
# threading1 = threading.Thread(target=double_numbers,args=(numbers,))
# threading2 = threading.Thread(target=square_numbers,args=(numbers,))
# threading1.start()
# threading2.start()
# threading1.join()
# threading2.join()
# end_time = time.time()
# print(f'Time taken: {end_time-begin_time}')


# Setting and Getting Name of Thread?
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