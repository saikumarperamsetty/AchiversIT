#Ex:1
class Student:
# for creating the Student Object
    def __init__(self,name,age,subject,marks,city):
        # self.name = 'sai'
        # self.age = 28
        # self.subject = 'python'
        # self.marks = 76
        # self.city = 'Bangalore'

        self.name = name
        self.age = age
        self.subject = subject
        self.marks = marks
        self.city = city

# for accepting the Student Object values
    def details(self):
        print('Hi My Name is ', self.name)
        print('Hi My age is ', self.age)
        print('Hi My subject is ', self.subject)
        print('Hi My marks are ', self.marks)
        print('Hi My city is ', self.city)

# we are creating instance off Student
# accecing the values directly with the method
# student1 = Student()
# student1.details()

# accecing the values directly with in the init method
stu1 = Student('Alice',24,'java',59,'USA')
print(stu1.name)
stu1.details()
print('\n')

# accecing the values directly with in the init method
stu2 = Student('Bob',21,'dotnet',59,'FRANCE')
print(stu2.name)
stu2.details()
print('\n')

# accecing the values directly with in the init method
stu3 = Student('SANIO ANDERSEN',19,'Python',45,'UK')
print(stu3.name)
stu3.details()