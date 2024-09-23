# List: it is ordered, mutable sequence of elements enclosed within [].
# =====
# important features of List[]:
# =============================
# --> mutable.
# --> preserve the insertion order.
# --> it can hold heterogenous elements.
# --> duplicate elements are allowed.
# --> dynamic

# 5 ways to create a List in Python?
# Ex:1 By Directly using the empty Square Brackets and append values to it?
# Type-1:
l = []
l.append('PERAMSETTY')
l.append('SAI')
l.append('KUMAR')
l.append(28)
print(l)
print(type(l))

# Ex:2 If we Know list values in Advance?
# Type-2:
l = [10,20,30,40,50]
print(l)
print(type(l))


# Ex:3 by splitting the String values?
# Type-3:
str = 'Learning Python is Very Easy'
s = str.split()
print(s)
print(type(s))


# Ex:4 by using list function?
# Type-4:
l = list([28,30,29])
print(l)
print(type(l))


# Ex:5 by using eval function?
# Type-5:
l = eval(input('Enter list values(by using eval):'))
print(l)
print(type(l))