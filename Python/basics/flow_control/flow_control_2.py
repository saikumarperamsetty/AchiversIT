# Nested Condition:
# definition = writing one condition inside another condition are called Nested Condition

# Ex:1 How to check a person is eligible for marriage and Adult by using Nested if else Condition?
age = 28
if age >= 18:
    print('You are Adult')
    if age >= 21:
        print('You are eligible for Marriage')
    else:
        print('You are Not eligible for Marriage')
else:
    print('You are minor')