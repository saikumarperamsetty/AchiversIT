# Task 1: Single Inheritance
class Animal:
    def sound(self):
        print('its sounding')
class Dog(Animal):
    def sound(self):
        print('dog barks..')
animal = Animal()
animal.sound()
dog = Dog()
dog.sound()

# Task 2: Multiple Inheritance
class Mother:
    def motherProfession(self):
        print('Mother is like God..')
class Father:
    def fatherProfession(self):
        print('Father is Like Instructor..')
class Child(Mother,Father):
    def childProfession(self):
        print('Child is Always not Listening Parents Words')
child = Child() 
child.motherProfession()
child.fatherProfession()
child.childProfession()

# Task 3: Multilevel Inheritance 
class Vehicle:
    def general_usage(self):
        print('Vehicle is for general usage.')
class Car(Vehicle):
    def special_usage(self):
        print('Car is for personal usage..')
class ElectricCar(Car):
    def eco_usage(self):
        print('ElectricCar is for environment friendly...')
e_car = ElectricCar()
e_car.eco_usage()
e_car.special_usage()
e_car.general_usage()

# Task 4: Calling Parent Class Method
class Person:
    def greet(self):
        print('Hello Good morning Person')
class Employee(Person):
    def greet(self):
        print('Hii Employee')

employee = Employee()
employee.greet()
person = Person()
person.greet()

# Task 5: Use of super() Keyword
class Shape:
    def __init__(self, shape_type):
        self.shape_type = shape_type
    def __str__(self):
        return f"Shape: {self.shape_type}"
class Circle(Shape):
    def __init__(self, radius):
        # Call the constructor of the parent class with a specific shape type
        super().__init__("Circle")
        self.radius = radius
    def __str__(self):
        return f"{super().__str__()}, Radius: {self.radius}"
# Example usage:
circle = Circle(28)
print(circle)

# Task 6: Hierarchical Inheritance
class Plant:
    def earth(self):
        print('Plants gives Oxyzen in nature.!')
class Tree(Plant):
    def grow(self):
        print('After plant Trees will grow')
class Flower(Plant):
    def give(self):
        print('Plants gives a Beautiful Flowers also')
tree = Tree()
tree.grow()
flower = Flower() 
flower.give()

# Hybrid Inheritance
# Ex:
# class Engine:
#     def engine_type(self):
#         print('This Car has a Petrol Engine')
# class Battery:
#     def battery_type(self):
#         print('It is 100kwh battery')
# class ElectricalVahicle(Engine,Battery):
#     def eco_friendly(self):
#         print('Electrical Vehicles are Environment Friendly..')
# class Vehical(ElectricalVahicle):
#     def fuel_efficient(self):
#         print('Vehicles are Fuel effivient')
# vehicle = Vehical()
# vehicle.engine_type()
# vehicle.battery_type()
# vehicle.eco_friendly()
# vehicle.fuel_efficient()

# Hirarchical Inheritance
# class Bird:
#     def lay_legs(self):
#         print('Birds has lay legs')
# class Sparrow(Bird):
#     def can_fly(self):
#         print('sparrow can Fly')
# class Penguine(Bird):
#     def can_swim(self):
#         print('Penguine can Swim')
# sparrow = Sparrow()
# sparrow.lay_legs()
# sparrow.can_fly()
# penguine = Penguine()
# penguine.lay_legs()
# penguine.can_swim()

# 7. Hybrid Inheritance Coding Challenge: University System
# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
# class Department:
#     def __init__(self,department_name):
#         self.department_name = department_name
#     def get_department(self):
#         # super().department_name
#         # return department_name
#         print('')
# class Professor(Person,Department):
#     def __init__(self, subject_specialization):
#         self.subject_specialization
#     def teach(self):
#         print('')
# class Administrator(Person,Department):
#     def __init__(self,role):
#         self.role=role
#     def manage(self,admin_duties):
#         self.admin_duties=admin_duties
# class TeachingAssistant(Person,Professor):
#     def assist(self):
#         print('')