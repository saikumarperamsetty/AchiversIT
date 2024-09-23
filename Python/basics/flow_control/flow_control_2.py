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
n = int(input('Enter Number to Print Triangle1:'))
for i in range(1,n+1):
    for j in range(1,i+1):
        print('*',end=' ')
    print()

# Approach-2
t = int(input('Enter Number to Print Triangle2:'))
for s in range(1,n+1):
    print('# '*s)