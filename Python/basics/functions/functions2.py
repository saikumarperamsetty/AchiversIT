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
def m3():
    z=12    #local variable
    print(z)
def m4():
    y=99
    print(y)    #local variable
    # print(z)    #Other function variable not able to access in m4
m3()
m4()