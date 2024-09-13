# Task 1: Single Inheritance
# class Animal:
#     def sound(self):
#         print('its sounding')
# class Dog(Animal):
#     def sound(self):
#         print('dog barks..')
# animal = Animal()
# animal.sound()
# dog = Dog()
# dog.sound()

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