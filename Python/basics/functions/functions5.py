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


# Ex:2 Basic Example of Indirect recursion in Python?
# def func1(n):
#     if n > 0:
#         print(n)
#         func2(n-1)
# def func2(n):
#     if n > 1:
#         print(n)
#         func1(n // 2)
# func1(10) #output = 10 9 4 3 1


# Ex:3 Basic Example of tail recursion in Python?
# def tail_recursion_factorial(n,accumalator=1):
#     if n == 0:
#         return accumalator
#     else:
#       return  tail_recursion_factorial(n-1,n*accumalator)
# result = tail_recursion_factorial(5)
# print(result)   #output = 120


# Ex:4 Basic Example of Iterative Approach in Python?
def iterative_factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
res = iterative_factorial(5)
print(res)  #output = 120