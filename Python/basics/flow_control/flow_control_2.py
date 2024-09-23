# Nested Condition:
# definition = writing one condition inside another condition are called Nested Condition

# Ex:1 How to check a person is eligible for marriage and Adult by using Nested if else Condition?
# age = 28
# if age >= 18:
#     print('You are Adult')
#     if age >= 21:
#         print('You are eligible for Marriage')
#     else:
#         print('You are Not eligible for Marriage')
# else:
#     print('You are minor')


# Ex:2 How to use Nested Loops?
# for i in range(4):
#     for j in range(4):
#         print('i',i,'j',j)


# Ex:3 How to print Triangle by using Nested Loops?
# Approach-1
# n = int(input('Enter Number to Print Triangle1:'))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print('*',end=' ')
#     print()

# # Approach-2
# t = int(input('Enter Number to Print Triangle2:'))
# for s in range(1,n+1):
#     print('# '*s)


# Ex:4 How to use Nested while Loops to print Triangle with number increasing pattern in Python?
# rows = 5
# i = 1
# while i <= rows:
#     j = 1
#     while j <= i:
#         print(j,end=' ')
#         j += 1
#     print()
#     i += 1


# break and continue Statements
# break: Used to terminate the loop and come out of the loop we can use this break statement.

# Ex:5 How to use break statement in a list in Python?
l = (20,10,40,30,50)
for i in l:
    if i == 40:
        print(i,'element find here')
        break
    print(i)