#Ex:1
class Student:
# for creating the Student Object
    def __init__(self):
        self.name = 'sai'
        self.age = 28
        self.subject = 'python'
        self.marks = 76
        self.city = 'Bangalore'

# for accepting the Student Object values
    def details(self):
        print('Hi My Name is ', self.name)
        print('Hi My age is ', self.age)
        print('Hi My subject is ', self.subject)
        print('Hi My marks are ', self.marks)
        print('Hi My city is ', self.city)

# we are creating instance off Student
# accecing the values directly with the method
student1 = Student()
student1.details()