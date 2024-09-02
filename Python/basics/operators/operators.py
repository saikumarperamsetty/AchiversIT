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