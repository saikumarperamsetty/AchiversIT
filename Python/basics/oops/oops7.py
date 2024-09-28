# Polymorphism:
# =============
# It refer to the ability or different classes to define methods that share the same name but have different implementation or behaviour.

# Ex:1 Basic Example of Polymorphism in Python?
# class Duck:
#     def talk(self):
#         print('Quack..Quack..')
# class Cat:
#     def talk(self):
#         print('Meow..Meow..')
# class Dog:
#     def talk(self):
#         print('Bow..Bow..')

# def f1(obj):
#     obj.talk()    
# l = [Duck(), Cat(), Dog()]
# for obj in l:
#     f1(obj)       # output = Quack..Quack..,Meow..Meow..,Bow..Bow..


# Ex:2 Polymorphism with hasattr() method in Python?
# class Duck:
#     def bark(self):
#         print('Quack..Quack..')
# class Cat:
#     def talk(self):
#         print('Meow..Meow..')
# class Dog:
#     def talk(self):
#         print('Bow..Bow..')

# def f1(obj):
#     if hasattr(obj, 'talk'):
#         obj.talk()
#     elif hasattr(obj,'bark'):
#         obj.bark()  
# l = [Duck(), Cat(), Dog()]
# for obj in l:
#     f1(obj)       # output = Quack..Quack..,Meow..Meow..,Bow..Bow..


# Overloading:
# ============
# Types Overloading:
# 1. Operator Overloading
# 2. Method Overloading
# 3. Constructor Overloading

# 1. Operator Overloading
# =======================
# class Book:
#     def __init__(self,pages):
#         self.pages = pages
#     def __add__(self,other):
#         return self.pages + other.pages
#     def __mul__(self,other):
#         return self.pages * other.pages
# book1 = Book(10)
# book2 = Book(20)
# print(book1+book2)        # output = 20
# print(book1*book2)        # output = 200

# 1.1 Operator Overloading with Two Diffrent Classes?
# class Employee:
#     def __init__(self,name,salary):
#         self.name = name
#         self.salary = salary
#     def __mul__(self,other):
#         return self.salary * other.days
# class Timesheet:
#     def __init__(self,days):
#         self.days = days
# obj1 = Employee('Sai Kumar',1300)
# obj2 = Timesheet(27)
# print(obj1*obj2)      # output = 241700


# 2. Method Overloading:
# ----------------------
# it is not supported in Python.
# Ex:1
# class Test:
#     def sum(self, a=None,b=None,c=None):
#         if a != None and b != None and c != None:
#             print('The Sum:',a+b+c)
#         elif a != None and b != None:
#             print('The Sum:',a+b)
#         else:
#             print('Provide two or more arguments')
# obj = Test()
# obj.sum(10,20,30)     # output = 60
# obj.sum(20,30)        # output = 50
# obj.sum(10)           # output = 10


# Ex:2 Method Overloading with *(args)?
# class Test:
#     def sum(self, *a):
#         total = 0
#         for x in a:
#             total = total + x
#         print('The Sum:',total)
# obj = Test()
# obj.sum(10,20,30)             # output = 60
# obj.sum(10,20)                # output = 30
# obj.sum(28)                   # output = Provide two or more arguments
# obj.sum(10,20,30,40,50)       # output = 150


# Ex: 1 Constructor Overloading:
# ===============================
# class Test:
#     def __init__(self):
#         print('No arg COnstructor')
#     def __init__(self,a):
#         print('1 arg COnstructor')
#     def __init__(self,a,b):
#         print('2 arg COnstructor')
# # obj2 = Test(10,20)            # output = 2 Arguments
# obj1 = Test(10)                 # output = TypeError: Test.__init__() missing 1 required positional argument: 'b'


# Overriding:
# 1. Method Overriding:
# 2. Constructor Overriding:

# 1. Example of Method Overriding?
# class Parent:
#     def __init__(self):
#         print('Money+Gold+Land')
#     def marry(self):
#         print('Kajal')
# class Child(Parent):
#     def marry(self):
#         super().marry()
#         print('Rishi')
# child = Child()
# child.marry()


# 2. Example of Constructor Overriding?
# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
# class Employee(Person):
#     def __init__(self,name,age,eno,esal):
#         super().__init__(name,age)
#         self.eno = eno
#         self.esal = esal
#     def details(self):
#         print('Emp Name: ',self.name)
#         print('Emp Age: ',self.age)
#         print('Emp no: ',self.eno)
#         print('Emp Salary: ',self.esal)
# employee = Employee('Sai Kumar',28,6963,62500)
# employee.details()


# Realtime Example of Polymorphism : Logistics Management System
class DeliveryMethod:
    def caluclate_cost(self,weight,distance):
        raise NotImplementedError('Subclasses Must implement this method')
class AirDelivery:
    def caluclate_cost(self,weight,distance):
        air_cargo_fee = 15.0
        cost = (weight * 5.0 + distance * 0.5)+air_cargo_fee
        return cost
class LandDelivery:
    def caluclate_cost(self,weight,distance):
        cost = (weight * 2.0 + distance + 0.1)
        return cost
class SeaDelivery:
    def caluclate_cost(self,weight,distance):
        container_fee = 30.0
        cost = (weight * 3.0 + distance + 0.3)+container_fee
        return cost
    
def caluclate_delivery_cost(delivery_method,weight,distance):
    return delivery_method.caluclate_cost(weight,distance)

if __name__ == '__main__':
    while True:
        print('Choose a Delevery Method')
        print('1. Air Deliver')
        print('2. Land Delivery')
        print('3. Sea Delivery')
        print('4. Exit')
        choice = int(input('Enter Your choice[1-4]:'))
        if choice in [1,2,3]:
            weight = float(input('Enter weight of your Delivery:'))
            distance = float(input('Enter distance of your Delivery:'))
            if choice == 1:
                method = AirDelivery()
            elif choice == 2:
                method = LandDelivery()
            elif choice == 3:
                method = SeaDelivery()
            cost = caluclate_delivery_cost(method,weight,distance)
            print(f'The Total Delivery Cost:{cost:.2f}')
        elif choice == 4:
            print('Executing the Program')
            break
        else:
            print('Invalid Choice you given...')