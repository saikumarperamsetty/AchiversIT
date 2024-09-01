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
