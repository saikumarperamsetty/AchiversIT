# Encapsulation in Python:
# Ex:1
class BankAccount:
    def __init__(self,balance):
        self.__balance = balance
    def get_balance(self):
        return self.__balance
    def set_balance(self,amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print('Amount Cannot be a Negative value...')
account = BankAccount(17092024)
print(account.get_balance())    #initially it is 17092024
account.set_balance(28)         #for set_balance we are setting a new balance
print(account.get_balance())    #after set_balance it is 28