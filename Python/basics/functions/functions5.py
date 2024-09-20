# Recursion in Python:
# Recursion: Recursion is a function which calls it self respectively, to solve a particular problem

# key concepts are:
# 1. Base case
# 2. Recursion case


# Ex:1 How to find Factorial using Recursive Function in Python?
# 1. Direct recursion
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)
# result = factorial(6)
# print(result)

# Types of Recursion Functions:
# 1. Direct recursion
# 2. Indirect recursion
# 3. Tail recursion

# 2. Basic Example of Indirect recursion in Python?
def func1(n):
    if n > 0:
        print(n)
        func2(n-1)
def func2(n):
    if n > 1:
        print(n)
        func1(n // 2)
func1(10)