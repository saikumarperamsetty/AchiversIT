# Regular Expressions:
# It is a declarative mechanism to represent a group of strings according to a particular format.

# Methods in Regular Expressions:
# 1. compile():
# 2. finditer():

# 1. compile():
# ===========
# i. start(): return the start index
# ii. end(): return the end index
# iii. group(): return the group index

# Ex:1 Basic Example to Pattern Find in Given String By Using Regular Expression?
# import re
# count = 0
# # pattern = re.compile('ab')
# matcher = re.finditer('ab','abaaababa')
# for match in matcher:
#     count += 1
#     print(match.start(),'....',match.end(),'....',match.group())    # output = 0 .... 2 .... ab, 4 .... 6 .... ab, 6 .... 8 .... ab
# print('The number of occurences of ab:',count)                      # output = 3


# Character Classes in Regular Expression:
# ========================================
# [abc] = only abc
# [^abc] = except abc
# [a-z] = only a-z
# [^a-z] = except a-z
# [A-Z] = ony A-Z 
# [^A-Z] = except A-Z 
# [a-zA-Z0-9] = only a-zA-Z0-9
# [^a-zA-Z0-9] = except a-zA-Z0-9

# Ex:2 Pattern Find in Given String By Using Character Classes in Regular Expression?
# import re
# x = '[abc]'
# x = '[^abc]'
# x = '[a-z]'
# x = '[^a-z]'
# x = '[A-Z]'
# x = '[^A-Z]'
# x = '[a-zA-Z0-9]'
# x = '[^a-zA-Z0-9]'
# pattern= re.compile(x)
# matcher = pattern.finditer('a7N@k9bTd2R8$')
# for match in matcher:
#     print(match.start(),'....',match.group())


# Predefined Character Classes in Regular Expression:
# ==================================================
# \s = only space
# \S = Except space, any other char
# \d = only digits
# \D = Except digits, any other char
# \w - it represents the Alpha_numeric, Except Special Chars
# \W - # Except Alpha_numeric, But only Special Chars
# \. - only dot(.)
# . - include dot(.) all other chars

# Ex:3 Pattern Find By Using Predefined Character Classes in Regular Expression?
# import re
# x = '\s'    #only space
# x = '\S'    #Except space, any other char
# x = '\d'    #only digits
# x = '\D'    #Except digits, any other char
# x = '\w'    #it represents the Alpha_numeric, Except Special Chars
# x = '\W'    # Except Alpha_numeric, only Special Chars
# x = '\.'    #only dot(.)
# x = '.'     #include dot(.), all other chars
# pattern= re.compile(x)
# matcher = pattern.finditer('a7N @k.9bT d2.R 8$')
# for match in matcher:
#     print(match.start(),'....',match.group())


# Quantifiers in Regular Expression:
# ==================================
# a = Exactly one time
# a+ = Min 1 time - Max any no of time
# a* = Min 0 time - Max any no of time
# a? = Min 0 time - Max 1 time
# a{m} = Exactly m time( m- means number we want to mention)
# a{m,n} = Exactly m,n time( m,n- means number we want to mention)


# Ex:4 Pattern Find By Using Quantifiers in Regular Expression?
import re
x = 'a'    # Exactly one time matching a string, it will return
x = 'a+'    # Min 1 time of a - Max any no of time of a, wherever a is came in String that will return
x = 'a*'    # Min 0 time of a - Max any no of time of a, wherever a is came in String that will return and include other chars(its hiding) also
x = 'a?'    # Min 0 time of a - Max 1 time of a, wherever a is came in String that will return
x = 'a{2}'    # Exactly m time( m- means number we want to mention), wherever a is came in String that will only return
x = 'a{2,5}'    # Exactly m,n time( m,n- means number we want to mention), wherever a is came in String that will only return
pattern= re.compile(x)
matcher = pattern.finditer('abaabaaab')
for match in matcher:
    print(match.start(),'....',match.group())