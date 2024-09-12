#Ex:1
class Student:
# for creating the Student Object
#Ex:2
    def __init__(self,name,age,subject,marks,city):
        #Ex:1
        self.name = 'sai'
        self.age = 28
        self.subject = 'python'
        self.marks = 76
        self.city = 'Bangalore'

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
#Ex:1
# accecing the values directly with the method
student1 = Student()
student1.details()

#Ex:2
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


# Constructor Function( init is Mandatory)
# Instance Function( init is not Mandatory otherthan any name you can take)
# Ex:3
print('\n')
class className():
    def __init__(self):
        print('Constructor Function Excuted.')
    def instance(self):
        print('Instance Function Excuted..')
obj = className()
obj.instance()

# Ex:4
print('\n')
class Employe:
    #constructor method
    def __init__(self):
        self.name = 'sai kumar'
        self.age = 28
        self.salary = 94000
        self.city = 'Bangalore'

    #Instance method
    def instanceMethod(self):
        self.name = 'SANIO ANDERSEN'
        self.age = 19

obj = Employe()
print(obj.__dict__)
obj.instanceMethod()
obj.city = 'UK'
print(obj.__dict__)

# Ex:4
# Local Variables: temporory variables
print('\n')
class Test:
    def m1(self):
        a = 10
        print(a)
    def m2(self):
        b = 20
        print(b)
test = Test()
test.m1()
test.m2()

# Ex:5
print('\n')
class Test1:
    def __init__(self):
        self.a = 10
        self.b = 20
        self.c = 30
    def m2(self):
        #accessing values in instance method
        print(self.a)
        print(self.b)
        #deleting values in instance method
        del self.c
        del self.b


obj = Test1()
obj1 = Test1()
obj2 = Test1()
#normal way to print values
obj.m2()
print(obj.__dict__)
obj.d = 40
print(obj.d)

obj1 = Test1()
obj2 = Test1()
del obj1.a  #if we delete in obj1 not effected in obj2
del obj2.b  #if we delete in obj2 not effected in obj1
print(obj1.__dict__)
print(obj2.__dict__)