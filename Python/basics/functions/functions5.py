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
# def iterative_factorial(n):
#     result = 1
#     for i in range(1, n+1):
#         result *= i
#     return result
# res = iterative_factorial(5)
# print(res)  #output = 120


# Memoization
# Ex:5 Basic Example of Memoization in Python?
# def fibonacci(n,memo={}):
#     if n in memo:
#         return memo[n]
#     if n <= 1:
#         return n
#     memo[n] = fibonacci(n-1,memo) + fibonacci(n-2,memo)
#     return memo[n]
# print(fibonacci(10))    #output = 55


# Ex:6 Sum of list elements in Python using Recusion?
# def sum_of_elements_list(lst):
#     if not lst:
#         return 0
#     else:
#         return lst[0] + sum_of_elements_list(lst[1:])
# print(sum_of_elements_list((1,2,3,4,5,6,7,8,9,10)))     #output = 55


# Ex:7 Reverse a String in Python using Recusion?
# def reverse_string(s):
#     if len(s) == 0:
#         return s
#     else:
#         return reverse_string(s[1:]) + s[0]
# print(reverse_string('Python'))     #output = onhtyp
# print(reverse_string('Sai Kumar'))  #output = ramuK iaS


# Ex:8 Given String is Palindrome or Not, in Python using Recusion?
# def palindrome_string(s):
#     if len(s) <= 1:
#         return True
#     if s[0] == s[-1]:
#         return palindrome_string(s[1:-1])
#     else:
#         return False
# print(palindrome_string('Python'))  #output = False
# print(palindrome_string('madam'))   #output = True
# print(palindrome_string('amanaplanacanalpanama'))   #output = True


# Ex:9 How to find Greatest Common Deviser(GCD) in Python using Recusion?
# def gcd(a,b):
#     if b == 0:
#         return a
#     else:
#         return gcd(b,a%b)
# print(gcd(28,48))   #output = 4
# print(gcd(20,0))   #output = 20


# Ex:10 How to find Flatten a List in Python using Recusion?
def flatten(lst):
    flat_list = []
    for item in lst:
        if isinstance(item,list):
            flat_list.extend(flatten(item))
        else:
            flat_list.append(item)
    return flat_list
print(flatten([1,[2,[3,4],5],6]))     #output = [1, 2, 3, 4, 5, 6]