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


# Ex:2 How to use Nested Loops?
for i in range(4):
    for j in range(4):
        print('i',i,'j',j)


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


# Ex:4 How to use Nested while Loops to print Triangle with number increasing pattern in Python?
rows = 5
i = 1
while i <= rows:
    j = 1
    while j <= i:
        print(j,end=' ')
        j += 1
    print()
    i += 1



# break and continue Statements
# break: Used to terminate the loop and come out of the loop we can use this break statement.

# Ex:5 How to use break statement in a list in Python?
l = (20,10,40,30,50)
for i in l:
    if i == 40:
        print(i,'element find here')
        break
    print(i)


# Ex:6 How to use continue statement in a list in Python?
cart = [30000,60000,20000,50000,40000]
for price in cart:
    if price >= 50000:
        print(price,'for thse Transactions You Need PAN CARD')
        continue
    print(price)


# Ex:7 How to print Even & Odd Numbers by using continue statement in Python?
# for Even Numbers:
for i in range(1,11):
    if i % 2 != 0:
        continue
    print(i)

# for Odd Numbers:
for j in range(1,11):
    if j % 2 == 0:
        continue
    print(j)


# Ex:8 How to print list values along with division by 100 by using continue statement in Python?
list = (10,20,0,50,40)
for i in list:
    if i == 0:
        print('How can you devide by Zero, I just Skipping this operation')
        continue
    print('100/{} = {}'.format(i,100/i))



# loops with else block:
# --> inside the loop execution, if the break statement is not executed,, then the else block will be executed.
# --> else means a loop without any break.
cart = [10,20,30,40,50]
for item in cart:
    if item >= 40:
        print('we cannot process this order..')
        break
    print(item)
else:
    print('Congrats.. All items processed Successfully...')



# pass Statement:
# --> empty statement
# --> null statement
# --> It will not do anything

# Ex:1 How to use pass statement in if block in Python?
if True:
            # without pass it's Giving Error
    pass    #  not giving any error 


# Ex:2 How to use pass statement in function in Python?
def function():
            # without pass it's Giving Error
    pass    #  not giving any error 
function()