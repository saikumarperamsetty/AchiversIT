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
class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.__salary = salary
    def __caluclate_bonus(self):
        return self.__salary * 1.0
    def show_emp_details(self):
        bonus = self.__caluclate_bonus()
        print(f'Employee:: Name:{self.name} Salary={self.__salary} Bonus={bonus}')

employee = Employee('Sai Kumar',62000)
employee.show_emp_details()
# print(employee._Employee__caluclate_bonus())   #This is Name Mangling in Python (It is not Recommended)