# Global Variable:
# Ex:
# p=28    #global variable
# def m1():
#     print(p)    #accessing global variable in m1
# def m2():
#     print(p)    #accessing global variable in m2
# m1()
# m2()

# Local Variable:
# Ex:
# def m3():
#     z=12    #local variable
#     print(z)
# def m4():
#     y=99
#     print(y)    #local variable
#     # print(z)    #Other function variable not able to access in m4
# m3()
# m4()

# Global Keyword:
# Ex:
# a=10
# def p1():
#     global b    #All b values are global now
#     b=28
#     # print(a)
#     print(b)
# def p2():
#     c=30
#     print(b)
# p1()
# p2()

# nonlocal Keyword:
# used in nested classes - neither global nor local
# Ex:
# def outer():
#     outer_var = 28
#     def inner():
#         nonlocal outer_var
#         outer_var +=1
#         print(outer_var)
#         print('inside Inner outer_var= ',outer_var)
#     inner()
#     print('inside Outer outer_var= ',outer_var)
# outer()


# Anonymous Function or lambda function
# definition: declaring a function without a name are called Anonymous function or lambda function 

# for Ex: Normal Function 
# def nf(h):
#     return h*h

# for Anonymous Function or lambda function
# lambda f: f*f

# Ex:1 by using lambda Expression find Square of a Number?
# square = lambda sq: sq*sq
# print('The Square of 28 is ',square(28))
# print('The Square of 82 is ',square(82))

# Ex:2 by using lambda Expression find sum of a two Numbers?
# sumOfTwoNums = lambda m,n : m+n
# print('Addition of 20 and 8 is ',sumOfTwoNums(20,8))
# print('addition of 4 and 13 is ',sumOfTwoNums(4,13))

# Ex:3 by using lambda Expression find biggest of a two Numbers?
# biggestOfTwoNums = lambda p,q : p if p>q else q
# print('between 20 and 8, the bigger Num is ',biggestOfTwoNums(20,8))
# print('between 28 and 82, the bigger Num is ',biggestOfTwoNums(28,82))

# filter() method in Python:
# Find Even Numbers and Odd Numbers in list in Python?
x = [1,2,3,4,5,6,7,8,9]
filtery = list(filter(lambda x: x%2==0,x))
print(filtery)

# map() method in Python:
# Definition: it will apply a function over each element in the sequence and the modified sequence
# Find the every number mul by 2, in list in Python?
m = [1,2,3,4,5,6,7,8,9,10]
mappy = list(map(lambda m:m*2,m))
print(mappy)

# reduce() method in Python:
# Definition: reduces the sequence of elements into asingle value and return that value 
# Find the every number mul by 2, in list in Python?
from functools import reduce
r = [1,2,3,4,5,6,7,8,9,10]
reduse = reduce(lambda a,b:a+b,r)
print(reduse)

# Function Alias
# Definition: for executing function, we can give the another name, it is called function alias.
# Ex:
def wish(name):
    print("Hello",name,'Good Night.!')
greeting = wish
wish('Sai')
print(id(wish))
print(id(greeting))
# del wish
wish('suraj')
greeting('madhuri')

# Nested Function
# Definition: writing one function inside another function is called nested function
def outer():
    print('outer function excution')
    def inner():
        print('inner function excuion')
    print('outer function calling inner function')
    return inner
res = outer()
# res = outer - function alias
# res = outer() - function calling and assigning return function 