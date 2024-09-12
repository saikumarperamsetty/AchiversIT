class Test:
    #static variable
    x = 10
    def __init__(self):
        #instance variable
        self.y = 20
t1 = Test()
t2 = Test()
print("t1:",t1.x,t2.y)
print("t2:",t1.x,t2.y)
Test.x = 888    #with the help of classname we are adding the value
t1.y = 999      #with the help of object reference we are adding the value & it is not changed
print("t1:",t1.x,t2.y)
print("t2:",t1.x,t2.y)