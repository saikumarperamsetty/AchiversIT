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
import re
x = '[abc]'
x = '[^abc]'
x = '[a-z]'
x = '[^a-z]'
x = '[A-Z]'
x = '[^A-Z]'
x = '[a-zA-Z0-9]'
x = '[^a-zA-Z0-9]'
pattern= re.compile(x)
matcher = pattern.finditer('a7N@k9bTd2R8$')
for match in matcher:
    print(match.start(),'....',match.group())