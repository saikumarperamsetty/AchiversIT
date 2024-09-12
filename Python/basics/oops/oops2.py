# Ex:1
# class Test:
#     #static variable
#     x = 10
#     def __init__(self):
#         #instance variable
#         self.y = 20
# t1 = Test()
# t2 = Test()
# print("t1:",t1.x,t2.y)
# print("t2:",t1.x,t2.y)
# Test.x = 888    #with the help of classname we are adding the value
# t1.y = 999      #with the help of object reference we are adding the value & it is not changed
# print("t1:",t1.x,t2.y)
# print("t2:",t1.x,t2.y)

#Different types of Accessing Static variable in Python
# Ex:2
class Test:
    a = 28
    def __init__(self):
        print(Test.a)

    def m1(self):
        print(Test.a)

    @classmethod
    def m2(cls):
        print(Test.a)
        print(cls.a)

    @staticmethod
    def m3():
        print(Test.a)

t = Test()
print(Test.a)
t.m1()
t.m2()
t.m3()