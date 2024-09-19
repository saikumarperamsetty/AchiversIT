# Abstraction in Python:
# Ex:1 Basic Example for Abstraction in Python?
# from abc import ABC, abstractmethod
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
#     @abstractmethod
#     def perimeter(self):
#         pass

# class Rectangle(Shape):
#     def __init__(self,width,height):
#         self.width = width
#         self.height = height
#     def area(self):
#         return self.width * self.height
#     def perimeter(self):
#         return 2 *(self.width + self.height)
    
# rectangle = Rectangle(28,29)
# print(rectangle.area())
# print(rectangle.perimeter())


# Ex:2 Payment System for E-commerse Website?
from abc import ABC,abstractmethod
class PaymentMethod:
    @abstractmethod
    def authonticate(self):
         """Authenticating the Payment Method"""
         pass
    @abstractmethod
    def ProcessPayment(self):
         """Prcess the payment with given amount"""
         pass
    @abstractmethod
    def refund(self):
         """Refunding the Amount"""
         pass
    
class CreditCard(PaymentMethod):
    def __init__(self,card_number,card_holder,cvv,expiry_date):
        self.card_number = card_number.replace(' ','').replace('-','')
        self.card_holder = card_holder
        self.cvv = cvv
        self.expiry_date = expiry_date

    def authonticate(self):
        if len(self.card_number) == 16 and self.cvv.isdigit() and len(self.cvv) == 3:
            print('Authenticating Credit Card Number: {self.card_number}')
            from datetime import datetime
            current_year = datetime.now().year % 100
            current_month = datetime.now.month
            exp_year,exp_month = map(int,self.expiry_date.split('/'))
            if (exp_year > current_year) or (exp_year == current_year and exp_month >= current_month):
                return True
            else:
                print('Sorry, Your Credit Card is Expired..')
                return False
        else:
            print('Invalid Credit Card Details..!')
            return False
        
    def ProcessPayment(self,amount):
        if self.authonticate():
            print(f'Processing Credit Card Payment of : {amount}')
            payment_successful = True
            if payment_successful:
                print('Processing Payment Successfully!')
                return True
            else:
                print('Payment Failed..')
                return False
        else:
            return False