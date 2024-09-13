# methods in class:
# 1. Instance methods
# 2. class methods
# 3. static methods

# 1. Instance methods
# Ex: 1
class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def display(self):
        print(f"Car: brand = {self.brand}, model = {self.model}")
car1 = Car('Maruti Car','bs-8')
# car1()
car1.display()

# Ex: 2
class Student:
    def __init__(self,name,age,marks):
        self.name = name
        self.age = age
        self.marks = marks
    def display(self):
        print(f"Student Name:{self.name}")
        print(f'Student Age:{self.age}')
        print(f"Student Marks:{self.marks}")
    def grade(self):
        if self.marks>90:
            return 'A'
        elif 80 <= self.marks <90:
            return 'B'
        elif 70 <= self.marks <80:
            return 'C'
        elif 60 <= self.marks <70:
            return 'D'
        else:
            return 'Fail'
        
student1 = Student('sai',28,83)
student2 = Student('suraj',33,93)
student3 = Student('madhavi',25,65)
student4 = Student('Alice',25,28)

student1.display()
print(f'Grade: {student1.grade()}')
student2.display()
print(f'Grade: {student2.grade()}')
student3.display()
print(f'Grade: {student3.grade()}')
student4.display()
print(f'Grade: {student4.grade()}')


# 2. class methods
# EX:3
class Car:
    total_cars = 0
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
        Car.total_cars +=1
    @classmethod
    def total(cls):
        print(f'Total Cars: {cls.total_cars}')
car1 = Car('Maruti','jreky')
car2 = Car('Toyota','krim')
car3 = Car('Skoda','prino')
car4 = Car('Tata','qeril')
Car.total()


# 3. Static methods
# EX:4
class MathOperation:
    @staticmethod
    def add(a,b):
        return a+b
    @staticmethod
    def mul(x,y):
        return x*y
mp = MathOperation()
print(mp.add(20,8))
print(mp.mul(10,28))

# Ex:5
class Engine:
    def __init__(self,horsepower):
        self.horsepower = horsepower
    def start(self):
        print(f"Engine with {self.horsepower} HP is started")
class Car:
    def __init__(self,brand,model,horsepower):
        self.brand = brand
        self.model = model
        self.engine = Engine(horsepower)
    def drive(self):
        print(f"Driving {self.brand} Car with, {self.model} model")
        self.engine.start()
car = Car(f'RANGEROVER','heigin',300)
car.drive()

# Inner Class:
# Ex:6
class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
        self.engine = self.Engine()
    class Engine:
        def start(self):
            print(f'Engine is started..')
    def display(self):
        print(f'Car: {self.brand} car with {self.model} model')
        self.engine.start()
car = Car('Maruti','Accord')
car.display()