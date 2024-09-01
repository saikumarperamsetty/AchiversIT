# Datatypes in Python
# Datatype is a type of data a variable is holding.

# List of Datatypes:
# 1. Primitive Datatypes:
# Number - int, float, complex
# str,
# boolean - True, False
# None

# list,
# tuple,
# dict,
# set,
# frozenset,
# range

# Examples for Number Datatypes:

# int Datatypes:
# 0, 1, -1
# decimal => default 0-9 
# binary => 0-1 0b or 0B will be prefixed
# octal => 0-7 0c or 0C will be prefixed
# hexaDecimal => 0-9a-f 0x or 0X will be prefixed

decimal = 10
print(decimal)
binary = 0B1100
print(binary)
octal = 0o73745633
print(octal)
hexaDecimal = 0x8374563391adfc
print(hexaDecimal)

# Base Conversion for binary - decimal, octal, hex values:
# Base Conversion for Decimal - bin, octal, hex values:
# Base Conversion for octal - bin, hex , decimal values:
# Base Conversion for hexadecimal - bin, octal, decimal values:

# Ex:
# bin()
binary = 0b1010
print(hex(binary))
print(oct(binary))
print(int(binary))

# decimal()
decimal = 28
print(hex(decimal))
print(oct(decimal))
print(int(decimal))

# octal()
octal = 0o1234567
print(hex(octal))
print(bin(octal))
print(int(octal))

# hex()
hex = 0x12345678adfb
print(bin(hex))
print(int(hex))
print(oct(hex))

# Float:
f = 28
print(type(f))

# Complex Datatype:
# Ex:
c = 28 + 24j
cd = 24 + 28j
print(c*cd)
print(c.real)
print(c.imag)
print(cd.real)
print(cd.imag)

# Boolean Datatype:
# Ex: True, False ==> keywords in python
# Ex: true, false ==> Its Just text in python
#  Boolean values are : 0, False, True, '', "",[],{},()

# Comparision Operator:
# ==, !=

# Ex:
print('sai' == 'sai')
print(29 != 28)
print(28 == 29)

# None Datatype:
# both a value and also be a datatype in python

# bytes Datatype in Python: utf-8 == uniform transformation format

b = b'Hello' #here b is suffix
print(b[0])  #it will give the "byte code values"

i = 'sai'
print(i)
print(type(i))
j = i.encode('utf-8')
print(j)
print(type(j))
k = j.decode('utf-8')
print(type(k))
print(k)

# bytearray Datatype:

# Ex1: with unicode values
byte_array = bytearray([65,66,67,68])
print(byte_array)
print(type(byte_array))

# Ex2: with string values
byte_array = bytearray('Hello','utf-8')
print(byte_array)

# Ex3: with b-prefix
byte_array = bytearray(b'Hello')
print(byte_array)

# Ex4: with index number changed(Modified)
byte_array = bytearray(b'Hello')
byte_array[0] = 67
print(byte_array)

# Ex5: with insert() method
byte_array = bytearray(b'belcome')
byte_array.pop(0)
# print(byte_array)
byte_array.insert(0,72)
print(byte_array)