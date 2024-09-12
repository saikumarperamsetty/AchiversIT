# Ex:1
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

#Different types of Accessing Static variable in Python
# Ex:2
print('\n')
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


# Ex:3
# Bank Operation in python
import sys
"""Bank Operation in Python"""
bankname = 'Stanchat Bank'
class Customer:
    def __init__(self,name,balance=0.0):
        self.name = name
        self.balance = balance

    def deposit(self,amt):
        self.balance = self.balance + amt
        print("Balance after DEPOSIT: ",self.balance)
    
    def withdraw(self,amt):
        if amt>self.balance:
            print("Insufficient Funds: cannot perform the Operation....")
            sys.exit()
            self.balance = self.balance - amt
            print("Balance after WITHDRAW: ",self.balance)
            
print("Welcome to Stanchat Bank")
name = input("Enter Your Name: ")
c = Customer(name)
while True:
        print("d-Deposit \nw-Withdraw \ne-Exit")
        option = input("choose your option: ")
        if option == 'd' or option == 'D':
            amt = float(input("Enter your amount:"))
            c.deposit(amt)
        elif option == 'w' or option == 'W':
            amt = float(input("Enter your amount: "))
            c.withdraw(amt)
        elif option == 'e' or option == 'E':
            print('Thank you for using the Application.!')
            sys.exit()
        else:
            print('Invalid Option. Please choose a valid Option..!')


# Ex: 4
# Local Variables in Python
print('\n')
class Temp:
    def m1(self):
        x = 28
        print(x)
    def m2(self):
        y = 29
        print(y)    #inside method we can access the Local Variable
        # print(x)    #outside method we can't access the Local Variable
obj = Temp()
obj.m1()
obj.m2()