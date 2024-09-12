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
sumOfTwoNums = lambda m,n : m+n
print('Addition of 20 and 8 is ',sumOfTwoNums(20,8))
print('addition of 4 and 13 is ',sumOfTwoNums(4,13))

# Ex:3 by using lambda Expression find biggest of a two Numbers?
biggestOfTwoNums = lambda p,q : p if p>q else q
print('between 20 and 8, the bigger Num is ',biggestOfTwoNums(20,8))
print('between 28 and 82, the bigger Num is ',biggestOfTwoNums(28,82))