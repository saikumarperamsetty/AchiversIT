# a-z, A-Z, _ these only are allowed in Python
name = 'PERAMSETTY SAI KUMAR' #valid
MyCourse = 'Python Full Stack' #valid
print(MyCourse)
print(name)

# 26082024python_ = 'batch started' #Invalid
_allowed = 'valid' #valid but it is private
__allowed = "valid" #strongly private
print(_allowed)
print(__allowed)

amount = 35000 #valid
# amou$nt = 1000000 #Invalid

name = 'SAI KUMAR PERAMSETTY' #valid
NAME = 'sai kumar peramsetty' #valid
print(name)
print(NAME)

# name$ = 'SAI KUMAR' #Invalid
N2AM8E = 'sai kumar p' #valid
# print(name$)
print(N2AM8E)

# Reserved Words:
# --> It has a special meaning and purpose.
# --> We cannot use them as identifiers.

import keyword
print(keyword.kwlist)