# Polymorphism: 
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
class Duck:
    def bark(self):
        print('Quack..Quack..')
class Cat:
    def talk(self):
        print('Meow..Meow..')
class Dog:
    def talk(self):
        print('Bow..Bow..')

def f1(obj):
    if hasattr(obj, 'talk'):
        obj.talk()
    elif hasattr(obj,'bark'):
        obj.bark()  
l = [Duck(), Cat(), Dog()]
for obj in l:
    f1(obj)