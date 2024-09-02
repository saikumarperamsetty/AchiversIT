# Oprators in Python:
# Types Of Operators are:
# 1. Arithmatic Operators
# 2. Relational Operators
# 3. Logical Operators
# 4. Assignment Operators
# 5. Ternary Operators
# 6. Bitwise Operators
# 7. Special Operators

# 1. Arithmatic Operators
# +, -, *, /

# 3. Logical Operators
# and ==> If both arguments are True then only result is True
# or ==> If atleast one argument is True then result is True
# not ==> Compliment

# Ex: and operator
x = 28
y = 29
comparision = (x < 29) and (y >28)
print(comparision)

# Ex: not operator
age = 15
can_vote = age >= 18
print(not can_vote)

# Ex: or operator
num1 = 28
num2 = 29
compare = (num1 >= 28) or (num2 < 30)
print(compare)

# Ex: Validating Login:
username = 'sai'
password = 'sai@1234'
validateLogin = (username == 'sai') and (password == 'sai@12345')
validateLogin1 = (username == 'sai') or (password == 'sai@12345')
print(validateLogin)
print(validateLogin1)


# 6. Bitwise Operators:
# Ex: +=, -=, *=, /=, ^=
balance = 3143
balance += 500
print(balance)


# 3. Logical Operators:
# and => True and  True = True
# or => True or False = True
# not => complementary --> it means if anything is True result is False, --> it means if anything is False result is True

# Ex: with boolean values
print(True and True)
print(True and False)
print(True)

# Ex: with non-boolean values
print(28 and 29 and 0 and 20) #0
print('' or 0 or "" or None) #none
print(not "") #false
print(not " ") #true

age = 14
vote = age >= 18
print(not vote)

# 6. Bitwise Operators:
# & = if both digits are 1 then the result is 1 else 0
# | = if atleast one of the digits is 1 then the result is else 0
# ^ = both digits must be different then the result is 1 else 0
# ~ = complementary
# << = bitwise left shift
# >> = bitwise right shift

# bitwise & operator:
# Ex:
print(4&5) #4
# 00000100
# 00000101
# res = 00000100 ==> 4

# bitwise & operator:
# Ex:
print(4&5) #4
# 00000100
# 00000101
# res = 00000100 ==> 4

print(5&8) #0
# 00000101
# 00001000
# res = 00000000 ==> 0

# bitwise | operator:
print(5|8) #13
# 00000101
# 00001000
# res = 00001101 ==> 13 if we convert into binary-> 0B1101 ==> 13

# bitwise ^ operator:
print(3^5) #6
# 00000011
# 00000101
# res = 00000110 ==> 6 if we convert into binary-> 0B0110 ==> 6

# bitwise ~ operator:
print(~5) #-6
# 00000101 => (binary representation)
# 11111010 => flipping
# 00000101+1(add one number) = -0110 ==> -6

# << = bitwise left shift Operator:
print(10<<2)
# 00001010 => 10
# 00101000 => after applying left shift (remove left side 00 and add right side 00)
print(0b00101000)

# >> = bitwise right shift Operator:
print(10>>2)
# 00001010 => 10
# 00000010 => after applying right shift (remove right side values of two digits and add left side values of two 00s)
print(0b00000010)

# 5. Ternary Operators: it is modern way of using if else
# syntax: value_if_true if condition else value_if_false
x = 28
y = 29
result = x if x < y else y
print(result) #28

a = 'apple'
b = 'banana'
res = a if len(a) < len(b) else b #apple
res = a if len(a) > len(b) else b #banana
print(res)

# How to check Number is Even or Odd number?
num = 28
resul = 'even' if num%2 == 0 else 'odd'
print(resul)

# How to check Number is divisible by 2 or not?
num = 28
resul = 'divisable' if num%2 == 0 else 'not divisable'
print(resul)

# 7. Special Operators (it is referring to the Address)
# 7.1 Membership Operators: in, not in
# 7.2 Identity Operators: is, is not

# Ex:
# 7.1 Membership Operators: in, not in
str = 'sai kumar JR NTR'
print('sai' in str)
print('sai ntr' in str)
print('Python' not in str)
print('JR NTR' not in str)

# Ex:
# 7.2 Membership Operators: iS, is not
str1 = 'apple'
str2 = 'apple'
print(id(str1))
print(id(str2))
print(str1 is str2)

str11 = 'apple'
str22 = 'APPLE'
print(id(str11))
print(id(str22))
print(str11 is not str22)