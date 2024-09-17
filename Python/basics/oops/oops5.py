# Encapsulation in Python:
# Ex:1 basic example of encapsulation in python
# class BankAccount:
#     def __init__(self,balance):
#         self.__balance = balance
#     def get_balance(self):
#         return self.__balance
#     def set_balance(self,amount):
#         if amount >= 0:
#             self.__balance = amount
#         else:
#             print('Amount Cannot be a Negative value...')
# account = BankAccount(17092024)
# print(account.get_balance())    #initially it is 17092024
# account.set_balance(28)         #for set_balance we are setting a new balance
# print(account.get_balance())    #after set_balance it is 28


# Ex:2 How Private Methods work in Python?
# class Employee:
#     def __init__(self,name,salary):
#         self.name = name
#         self.__salary = salary
#     def __caluclate_bonus(self):
#         return self.__salary * 1.0
#     def show_emp_details(self):
#         bonus = self.__caluclate_bonus()
#         print(f'Employee:: Name:{self.name} Salary={self.__salary} Bonus={bonus}')

# employee = Employee('Sai Kumar',62000)
# employee.show_emp_details()
# # print(employee._Employee__caluclate_bonus())   #This is Name Mangling in Python (It is not Recommended)


# Ex:3 Name Mangling in Python?
# class Test:
#     def __init__(self):
#         self.__private_var = 'I am From Private'
#     def get_private_var(self):
#         return self.__private_var
# obj = Test()
# print(obj.get_private_var())
# # print(obj.__private_var)      # directly we are not able to Access the Private method through object
# print(obj._Test__private_var)   # directly we Can Access the Private method through object, it is Called Name-Mangling


# Ex:4 Encapsulation in Car System?
class Car:
    def __init__(self,speed=0,fuel=100,engine_status=False):
        self.__speed = speed
        self.__fuel = fuel
        self.__engine_status = engine_status

    def get_speed(self):
        return self.__speed
    
    def set_speed(self,speed):
        if self.__engine_status:
            if 0 <= speed <=240:
                self.__speed = speed
            else:
                print('Invalid Speed Range! Speed Must be 0 t0 240')
        else:
            print('Cannot Start the Engine! Because NO FUEL in the Car..')

    def get_fuel(self):
        return self.__fuel

    def set_fuel(self,fuel):
        if self.__fuel:
            if 0 <= fuel <= 100:
                self.__fuel = fuel
            else:
                print('Invalid Fuel Range! fuel Must be 0 to 100')
    
    def start_engine(self):
        if self.__fuel > 0:
            self.__engine_status = True
            print('Engine Started')
        else:
            print('Cannot Start the Engine! Because No FUEL')

    def stop_engine(self):
        if self.__engine_status:
            self.__engine_status = False
            self.__speed = 0
            print('Engine Stopped')
        else:
            print('Cannot Stop the Engine!, Because the Engine is Already OFF')
    def car_status(self):
        status = 'ON' if self.__engine_status else 'OFF'
        print(f'Engine::{status} Speed:{self.__speed}km/h Fuel:{self.__fuel}%')

my_car = Car()
my_car.car_status()
# my_car.set_speed(40)
my_car.start_engine()
my_car.set_speed(40)
my_car.car_status()
my_car.set_fuel(95)
my_car.car_status()