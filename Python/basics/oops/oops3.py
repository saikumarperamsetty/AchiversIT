# methods in class:
# 1. Instance methods
# 2. class methods
# 3. static methods

# 1. Instance methods
# Ex:
class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def display(self):
        print(f"Car: brand = {self.brand}, model = {self.model}")
car1 = Car('Maruti Car','bs-8')
# car1()
car1.display()