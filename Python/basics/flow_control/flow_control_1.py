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
l = [10,20,30,40,50]
sum = 0
for i in l:
    sum = sum+i
    print('The Sum: ',sum)