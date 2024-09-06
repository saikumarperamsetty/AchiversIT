# Exception = An event that inturrept the flow of program
# types = (ZeroDivisionError, TypeError, ValueError)

# Ex:1
# ZeroDivisionError:
1 / 0       #ZeroDivisionError

# Ex:2
# TypeError
1 + "python programming"    #TypeError

# Ex:3
# ValueError
int("python exception handling")    #ValueError

# Ex:4 What is try, except, finally in python?
try:
    number = int(input("Enter a Number:"))
    print(1 / number)
except ZeroDivisionError:
    print("You cant't devide by Zero!")
except TypeError:
    print("Please Enter numbers only")
finally:
    print("This will do the Cleanup Activities..!")