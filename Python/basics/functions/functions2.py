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
a=10
def p1():
    global b    #All b values are global now
    b=28
    # print(a)
    print(b)
def p2():
    c=30
    print(b)
p1()
p2()