# Exception = An event that inturrept the flow of program
# types = (ZeroDivisionError, TypeError, ValueError)

# Ex:1
# ZeroDivisionError:
# 1 / 0       #ZeroDivisionError

# Ex:2
# TypeError
# 1 + "python programming"    #TypeError

# Ex:3
# ValueError
# int("python exception handling")    #ValueError

# Ex:4 What is try, except, finally in python?
# try:
#     number = int(input("Enter a Number:"))
#     print(1 / number)
# except ZeroDivisionError:
#     print("You cant't devide by Zero!")
# except TypeError:
#     print("Please Enter numbers only")
# finally:
#     print("This will do the Cleanup Activities..!")

#Ex: 5
# def devide(x,y):
#     try:
#         result = x / y
#     except ZeroDivisionError:
#         print("You can't devide by ZERO")
#     else:
#         print("result = ", result)
#     finally:
#         print("finally Block is Excuted at the end!")
# devide(28,7)
# devide(28,2)


# Ex:6 How to handle Different types Exceptions?
# try:
#     print('Welcome to Exception Handling..')
#     print(x)
#     print(10/0)
#     print(10/'ten')
# except ZeroDivisionError:
#     print('Zero Division Error')
# except TypeError:
#     print('Type Error')
# except NameError:
#     print('Name Error')


# Ex:7 How to input from cmd prompt handle Different types Exceptions?
# try:
#     x = int(input('Enter x value:'))
#     y = int(input('Enter y value:'))
#     print(x/y)
# except ArithmeticError:
#     print('Arithmetic Error')
# except ZeroDivisionError:
#     print('Arithmetic Error')


# Ex:8 try except blocks with inner try except block?
try:
    print('Statement-1')
    # print('Statement-2')
    print(10/2)
    print('Statement-3')
    try:
        print('Statement-4')
        print('Statement-5')
        print('Statement-6')
    except:
        print('Statement-7')
except:
    print('Statement-8')
finally:
    print('Statement-9')
        