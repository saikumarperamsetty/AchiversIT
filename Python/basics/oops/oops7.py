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
#     f1(obj)


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
#     f1(obj)


# Overloading:
# ============
# Types Overloading:
# 1. Operator Overloading
# 2. Method Overloading
# 3. Constructor Overloading

# 1. Operator Overloading
class Book:
    def __init__(self,pages):
        self.pages = pages
    def __add__(self,other):
        return self.pages + other.pages
    def __mul__(self,other):
        return self.pages * other.pages
book1 = Book(10)
book2 = Book(20)
print(book1+book2)
print(book1*book2)