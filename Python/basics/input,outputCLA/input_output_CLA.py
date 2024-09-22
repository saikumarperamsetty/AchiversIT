# Input, Output and CLA
# Input = raw_input('Enter Some Value')   #Python 2 series
# print(Input)

# Input = input('Enter Some value:')   #Python 3 series
# print(type(Input))  #by Default type is str


# Ex:1  How to add Two Numbers taking input from user?
# x = input('Enter First Number:')    #10
# y = input('Enter Second Number:')   #20
# # # print(x+y)      # output = 1020 --> it treated like Concatination
# p = int(x)
# q = int(y)

# #Approach-1 to print input
# print('The Sum is: ',p+q)      # output = 30


# Ex:2  How to add Two Numbers taking input from user?
#Approach-2 to print input
# print('The Sum is: ',int(input('Enter First Number:'))+int(input('Enter Second Number:')))  # 28 29 = 57


# Ex:3  How to add Two Strings taking input from user?
# str1 = input('Enter First String:')    #SAI
# str2 = input('Enter Second String:')   #KUMAR
# print('Result :', str1+str2)    #SAIKUMAR


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