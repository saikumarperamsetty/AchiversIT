# Input, Output and CLA
# Input = raw_input('Enter Some Value')   #Python 2 series
# print(Input)

Input = input('Enter Some value:')   #Python 3 series
print(type(Input))  #by Default type is str


# Ex:1  How to add Two Numbers taking input from user?
# #Approach-1 to print input
x = input('Enter First Number:')    #10
y = input('Enter Second Number:')   #20
# # print(x+y)      # output = 1020 --> it treated like Concatination
p = int(x)
q = int(y)
print('The Sum is: ',p+q)      # output = 30


# Ex:2  How to add Two Numbers taking input from user?
#Approach-2 to print input
print('The Sum is: ',int(input('Enter First Number:'))+int(input('Enter Second Number:')))  # 28 29 = 57


# Ex:3  How to add Two Strings taking input from user?
str1 = input('Enter First String:')    #SAI
str2 = input('Enter Second String:')   #KUMAR
print('Result :', str1+str2)    #SAIKUMAR


# Ex:4   How to take input from user for the Employee info?
eno = int(input('Enter your Eno: '))
ename = input('Enter your Name: ')
esalary = int(input('Enter your Esalary: '))
eaddr = input('Enter your Address: ')
married = input('Married[True/False]: ').strip().lower() == 'true'
print('please confirm Employee details.?')
print('Emp No:',eno)
print('Emp Name:',ename)
print('Emp Salary:',esalary)
print('Emp Address:',eaddr)
print('Emp Married:',married)


# Ex:5   How to take Two input numbers in same line from input?
i,j = map(int,input('Enter Two Numbers:').split())
product = i * j # 10 20
print(product)      # output = 200


# Ex:6   How to use eval() method with the help from input?
eval1 = eval('10+20+30+40')        # output = 100
eval2 = eval('10.6+20.4+30.2')      # output = 61.2
eval3 = eval('99+28+30+True')  #here True=1(within the String)     # output = 157+(True) ==> 158
# eval4 = eval('10+20+30+SAI')      # output = NameError: name 'SAI' is not defined
print(eval1)
print(eval2)
print(eval3)
# print(eval4)

list1 = eval(input('Enter Some List Values: '))
print(list1)
print(type (list1))
print(sum(list1))


# Ex:7  How to use print() method in different ways in PYTHON?
print('SaiKumar')   # output = SaiKumar
print('Sai\tKumar') # output = Sai  Kumar (\t = its giving tab space=)
print('Sai\nKumar') # output = Sai  \nKumar (\n = its coming in new line)

# # repetion_operator: (*) means one value should be String and value Should be Int 
print('SAI KUMAR'*3)    # output = SAI KUMARSAI KUMARSAI KUMAR (it will print 3times)

# # concatination_operator: (+) it will add Two Strings 
print('SAI'+'KUMAR')    # output = SAIKUMAR

print('SAI KUMAR'+10)    # output = it will Give TYPE ERROR --> TypeError: can only concatenate str (not "int") to str

# comma operator(,) ==>here comma(,) seperates the space( ) --> This Comma(,) not there in JavaScript, But we can we can use both comma(,) and plus(+) in Python.
print('PEARMSETTY','SAI KUMAR')     # output = PEARMSETTY SAI KUMAR (here comma(,) seperates the space( ) in the output)

# Ex:8  How to use Destructuring in Python?
p,q,r = 28,29,30
print('The Destructered Values are: ', p,q,r)   # output = The Destructered Values are:  28 29 30  # here comma(,) giving the space in the output

# Ex:9  How to use end= operator in Python?
print('PERAMSETTY',end=' ')     #   here end= operator is it will all print results in Same line
print('SAI',end=' ')            # here end= operator is it will all print results in Same line
print('KUMAR')              # output = PERAMSETTY SAI KUMAR

# Ex:10     print() for list,tuple and int?
list
list2 = (10,20,30,40,50)
print(list2)
print(type(list2))

# tuple
tuple1 = 10,20,30,40,50
print(tuple1)
print(type(tuple1))

# int
int1 =28
print(int1)
print(type(int1))


# Command Line Arguments(CLA):
import sys
print('Script Name:',sys.argv[0])
print('Arguments:',sys.argv[1:])


import argparse
parser = argparse.ArgumentParser(description='CLA Demonstration:')
parser.add_argument('name',help='Your Name')
parser.add_argument('age',int,help='Your Age')
parser.add_argument('--greet',action='store_true',help='Greet the User')

args = parser.parse_args()
if args.greet:
    print(f'Hi {args.name}! {args.age} years old..')
else:
    print(f'{args.name},{args.age}')