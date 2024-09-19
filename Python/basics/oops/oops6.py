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