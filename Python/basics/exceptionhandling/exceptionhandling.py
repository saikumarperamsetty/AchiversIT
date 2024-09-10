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

#Ex: 5
def devide(x,y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("You can't devide by ZERO")
    else:
        print("result = ", result)
    finally:
        print("finally Block is Excuted at the end!")
devide(28,7)
devide(28,2)