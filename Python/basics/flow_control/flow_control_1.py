# Flow Control-1:
# Flow Control: flow is the order in which the statements are executed.
# Conditions: if elif else 
# Loops : for, while
# Transfer Statements or Loop Controls: break, continue and pass


# Conditions: if elif else 
# Ex:1 if else
# marks = 83
# if marks >= 35:
#     print('You Passed the Exam.!!')
# else:
#     print('Sorry, You Failed the Exam...!')


# Ex:2 if else elif
# temp = 4
# if temp >= 28:
#     print("It's, Hot Outside")
# elif temp >= 12:
#     print("It's, Cool Outside")
# elif temp >= 5:
#     print("It's, Freezing Cold Outside")
# else:
#     print("Don't go Outside..?")


# Ex:3 if else --> specially for name matches
# name = input('Enter Your Name: ')
# if name == 'SAI KUMAR':
#     print('Hi',name,'Good Evening')
#     print('Have a Great Day ahead..')
# else:
#     print('Hello Guest, Good night..')


# Ex:4 How to Find Biggest Number by using if,else and elif?
# num1 = input('Enter num1: ')
# num2 = input('Enter num2: ')
# num3 = input('Enter num3: ')
# if num1 > num2 and num1 > num3:
#     print('num1 is the Biggest')
# elif num2 > num3:
#     print('num2 is the Biggest')
# else:
#     print('num3 is the Biggest')


# Loop or Iterative Statements:
# for : It can be used to iterate over the Sequence, and execute some action.
# while : It will execute as long as the Condition is true.

# for loop Examples:
# Ex:1  How to iterate over a String by using for loop in Python?
# str = 'SAI KUMAR'
# for char in str:
#     print(char)     # output = vertical output
#     print(char,end=' ') # output = Horizontal output --> S A I   K U M A R


# Ex:2  How to iterate over a list by using for loop in Python?
# list1 = (13,25,69,75,18,77,8)
# for l in list1:
#     print(l)

# Ex:3 How to iterate over a tuple and Find the Sum value by using for loop in Python?
# l = [10,20,30,40,50]
# sum = 0
# for i in l:
#     sum = sum+i
#     print('The Sum: ',sum)


# Ex:4 How to print Even and Odd numbers by using for loop in Python?
# # For Odd Numbers:
# for j in range(1,11,2):
#     print(j)

# For Even Numbers:
# for j in range(10,0,-2):
#     print(j)


# while loop Examples:
# Ex:1  How to print first 10 numbers by using while loop in Python?
# x = 0
# while x <=9:
#     x += 1
#     print(x)


# Ex:2  How to print the Sum of n numbers by using while loop in Python?
# n = int(input('Enter a number to find the total:'))
# sum = 0
# x = 1
# while x < n:
#     sum = sum+x
#     x += 1
# print("The Sum of first",n,'numbers is = ',sum)


# Ex:3  How to create infinite loop by using while loop in Python?
name = ""
while name != 'sai kumar':
    name = input('Enter Matching Name: ')
print('Thanks for giving the Matching Name..!')