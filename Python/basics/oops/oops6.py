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
class PaymentMethod(ABC):
    @abstractmethod
    def authenticate(self):
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
    
class CreditCardPayment(PaymentMethod):
    def __init__(self, card_number, card_holder, cvv, expiry_date):
        self.card_number = card_number.replace(' ','').replace('-','')
        self.card_holder = card_holder
        self.cvv = cvv
        self.expiry_date = expiry_date

    def authenticate(self):
        if len(self.card_number) == 16 and self.cvv.isdigit() and len(self.cvv) == 3:
            print(f'Authenticating Credit Card Number: {self.card_number}')
            from datetime import datetime
            current_year = datetime.now().year % 100
            current_month = datetime.now().month
            exp_month, exp_year = map(int,self.expiry_date.split('/'))
            if (exp_year > current_year) or (exp_year == current_year and exp_month >= current_month):
                return True
            else:
                print('Sorry, Your Credit Card is Expired..')
                return False
        else:
            print('Invalid Credit Card Details..!')
            return False
        
    def ProcessPayment(self,amount):
        if self.authenticate():
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
        
    def refund(self,amount):
        print(f'Refunding Rs.{amount} to Credit Card {self.card_number}')
        refund_successfull = True
        if refund_successfull:
            print('Refunding Successfull')
        else:
            print('Refund Failed..')
            return False
        
class PaypalPayment(PaymentMethod):
    def __init__(self,email):
        self.email = email

    def authenticate(self):
        if '@' in self.email and '.' in self.email.split('@')[-1]:  #mypayment@example.com
            print(f'Authenticating Paypal account of email: {self.email}')

            authenticated = True
            if authenticated:
                return True
            else:
                print('Authentication failed')
                return False
        else:
            print('Invalid Paypal Email address')
            return False
        
    def ProcessPayment(self,amount):
        if self.authenticate():
            print(f'Processing Paypal Payment of Amount: {amount}')
            payment_successful = True
            if payment_successful:
                print('Processing Payment Successfully')
                return True
            else:
                print('Payment Failedd')
                return False
        else:
            print('payment failed, because of Authentication Error')
            return False
        
    def refund(self,amount):
        print(f'Refunding Amount Rs{amount} to Paypal account of :{self.email}')
        refund_successful = True
        if refund_successful:
            print('Refunding Processed Successfully..')
            return True
        else:
            print('Refund Failed...')
            return False
        
def complete_purchase(payment_method,amount):
    if payment_method.authenticate():
        if payment_method.ProcessPayment(amount):
            print('Payment Successful')
        else:
            print('Payment Failed')
    else:
        print('Authentication Failed')

credit_card_payment = CreditCardPayment(
    card_number = '1234567891234567',
    card_holder = "Sai Kumar",
    cvv = "123",
    expiry_date = '12/26'
)

paypal_payment = PaypalPayment(email="saikumar28p@gmail.com")

complete_purchase(credit_card_payment, 1500)
complete_purchase(paypal_payment, 2000)