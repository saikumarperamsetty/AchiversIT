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
import re
count = 0
# pattern = re.compile('ab')
matcher = re.finditer('ab','abaaababa')
for match in matcher:
    count += 1
    print(match.start(),'....',match.end(),'....',match.group())    # output = 0 .... 2 .... ab, 4 .... 6 .... ab, 6 .... 8 .... ab
print('The number of occurences of ab:',count)                      # output = 3