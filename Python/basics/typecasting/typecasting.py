# Type Casting in Python:
# Type Casting in Python is Converting from one Datatype to another datatype.

# Why Typecasting?
# 1. Data Compatability:
# Ex:
age = 28
message = 'Hii My Name is Sai Kumar, my Age is '+str(age)+'.'
# message = 'Hii My Name is Sai Kumar, my Age is '+age+'.' #it will TypeError
print(message)

# 2. Precision and Performance:
# Ex:
percentage = 72.54
percentage_with_int = int(percentage)
print(percentage_with_int)

# 3. Data Transformation:
# Ex:
import csv
with open('emp.csv','r') as file:
    data = csv.reader(file)
    for row in data:
        value = int(row[0])


# 4. Interoperability:
# Ex:
import json
data = {'name':'sai','age':25}
print(type(data))
json_data = json.dumps(data)
print(type(json_data))


# Two Types of Typecasting:
# 1. Implicit Typecasting
# 2. Explicit Typecasting

# Different kinds of typecasting in Python:
int()
float()
str()
bool()
bytes()
bytearray()
complex()
dict()
list()
set()
tuple()

# 1. Implicit Typecasting(Normal)
# Ex:
n1 = 10
n2 = 28.5
print(n1+n2)


# 1. Explicit Typecasting(difficult)
# Ex: int() conversion
print(int(28.7))
print(int('10'))
print(int('ten')) #not convret
print(int(2+7j)) #not convret
print(int(True))
print(int(False))
print(int(0o776))
print(int('10.5')) #not convert
print(int('10'))

# Ex: float() conversion
print(float(28))
print(float('10'))
print(float('ten')) #not convret
print(float(2+7j)) #not convret
print(float(True))
print(float(False))
print(float(0x786ADF))
print(float('10.5'))

# Ex: str() conversion : WE CAN CONVERT ANY TYPE TO STRING
print(str(28))
print(str('10'))
print(str('ten')) #not convret
print(str(2+7j)) #not convret
print(str(True))
print(str(False))
print(str(0o756))
print(str('10.5'))

# Ex: bool() conversion
print(bool(28))
print(bool('10'))
print(bool('ten'))
print(bool(2+7j))
print(bool(True))
print(bool(False))
print(bool(0b1000))