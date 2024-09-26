# Dictonary datatype:
# =====================
# dictonary is an unordered collections of datatype in python where we can store the data in the form of key, values pairs.

# Key feaytures of dictonary:
# ===========================
# dynamic.
# mutable.
# it is unorderd.
# it will not allow indexing and slicing.
# Keys cannot be duplicated, but values will be duplicated.


#Ex:1 How to create dictonary in Python?
# by using dictonary values in advance?
d = {1:'SAI KUMAR',2:'SURAJ',3:'NTR'}
d[1] = 'PERAMSETTY SAI KUMAR'
d[3] = 'JR NTR'
print(d)

#Ex:2 by using dict() function with list of tuples to create a dictonary?
d = dict([(1,'Alice'),(2,'Bob'),(3,'John')])
print(d[3])       # output = John
print(d[30])    # output = KeyError: 30
print(d)

#Ex:3 membership operators in dictonary in Python?
d = {1:'SAI KUMAR',2:'SURAJ',3:'NTR'}
if 3 in d:
    print(d[1])     # output = SAI KUMAR
if 10 in d:
    print(d[3])     # output = empty output