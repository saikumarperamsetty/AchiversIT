# Syntax of Function
# def functionName():
#     -----

# # Ex:1
# def greet(name):
#     print('Hii',name,'Good Evening to All..! I am From greet Function')
# greet('sai')

# #Ex:2
# def square(x):
#     print('\nSquare of ',x ,'is =', x * x)
# square(7)

# #Ex:3
# print('\n')
# def add(i,j):
#     print('addition = ',i+j)
# def mul(i,j):
#     print('multiplication = ',i*j)
# add(20,8)
# mul(28,33)

# #Ex:4
# print('\n')
# def add(a,b):
#     sum = a+b
#     return sum
# result = add(20,8)
# print(result)

#Ex:5
# How to Print Even or Odd Numbers in Python?
# def even_odd(num):
#     if num % 2 == 0:
#         print("Even Number")
#     else:
#         print("Odd Number")
# even_odd(28)
# even_odd(29)


# How to work with Arguments in Python?
# Arguments:
# 1.Positional Arguments:
#Ex:6
# def sum(a,b):
#     print(a+b)
# sum(20,8)

# 2.keyword Arguments:
#Ex:7
# def wish(name,msg):
#     print("Hello",name,msg)
# wish(msg='Having great day Ahead..!',name='Sai Kumar')

#Ex:8
# def calc(x,y):
#     print(x+y)
#     print(x-y)
# calc(y=11,x=42)

# 3.Default Arguments:
# Ex:9
# def wish(msg,name='Guest'):
#     print('Hello',name,msg)
# wish(name='Sai Kumar',msg='Thank you')

# 3.Variable Length Positional Arguments:(*)
# Ex:10
# def f1(*n):
#     total = 0
#     for i in n:
#         total = total + i
#         print("The Sum =",total)
# f1(10,20,30)

# 3.Variable Length Keyword Arguments:(**kwargs)
# Ex:10
def demo(**kwargs):
    for k,v in kwargs.items():
        print(k, '=', v)
demo(e1=28,e2=33,e3=25)
demo(name='sai',age=28,subject='python')