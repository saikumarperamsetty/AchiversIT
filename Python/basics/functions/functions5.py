# Recursion in Python:
# Recursion: Recursion is a function which calls it self respectively, to solve a particular problem

# key concepts are:
# 1. Base case
# 2. Recursion case

# Ex:1 How to find Factorial using Recursive Function in Python?
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
result = factorial(6)
print(result)