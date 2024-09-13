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