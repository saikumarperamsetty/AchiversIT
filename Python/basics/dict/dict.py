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
# d = {1:'SAI KUMAR',2:'SURAJ',3:'NTR'}
# d[1] = 'PERAMSETTY SAI KUMAR'
# d[3] = 'JR NTR'
# print(d)


#Ex:2 by using dict() function with list of tuples to create a dictonary?
# d = dict([(1,'Alice'),(2,'Bob'),(3,'John')])
# print(d[3])       # output = John
# print(d[30])    # output = KeyError: 30
# print(d)


#Ex:3 membership operators in dictonary in Python?
# d = {1:'SAI KUMAR',2:'SURAJ',3:'NTR'}
# if 3 in d:
#     print(d[1])     # output = SAI KUMAR
# if 10 in d:
#     print(d[3])     # output = empty output


# Ex:4 dict{} with Student marks info Example?
# rec = {}
# n = int(input('Enter no of Students:'))
# i = 1
# while i <= n:
#     name = input('Enter Student Name:')
#     marks = int(input('Enter Student marks:'))
#     rec[name] = marks 
#     i += 1
# print('Name of Student:','\t','% of marks')
# for x in rec:
#     print('\t',x,'\t\t',rec[x])


#Ex:5 Different type of methods in dict{}?
# ==========================================
# get() method in dict{}
# d = {1:'A',2:'B',3:'C'}
# print(d.get(2))                                 # output = B, if there is value presented in dict, it wii give that value
# print(d.get(4,'no value for this dictonary'))   # output = None, if there is no value presented in dict, it wii give 'None'


# pop() method in dict{}
# d = {1:'A',2:'B',3:'C'}
# d.pop(1)    # it will remove that particular item only
# d.pop(5)    # if element not there in dict{}, it will give KeyError
# print(d)    # output = {2: 'B', 3: 'C'}


# popitem() method in dict{}
# d = {1:'A',2:'B',3:'C'}
# d.popitem()    # it will remove that last item only in the dict{}
# d.popitem()    # it will remove that last item only in the dict{}
# d.popitem()    # it will remove that last item only in the dict{}
# d.popitem()    # if dict{} is empty, then also we are trying to use popitem() method it will give KeyError: 'popitem(): dictionary is empty'
# print(d)


# copy() method in dict{}
# d = {1:10, 2:20, 3:30, 4:40}
# copied_dict = d.copy()
# d[2] = 200              # Here d[2] = 200 is updated the dict{} value
# print(d)                # output = {1: 10, 2: 200, 3: 30, 4: 40}
# print(copied_dict)      # output = {1: 10, 2: 20, 3: 30, 4: 40}


# keys() method in dict{}
# d = {1:'A',2:'B',3:'C'}
# print(d.keys())             # output = dict_keys([1, 2, 3]), it will give only keys


# values() method in dict{}
# d = {1:'A',2:'B',3:'C'}
# print(d.values())             # output = dict_values(['A', 'B', 'C']), it will give only values


# items() method in dict{}
# d = {1:'A',2:'B',3:'C'}
# print(d.items())             # output = dict_items([(1, 'A'), (2, 'B'), (3, 'C')]), if we want to convert dict items to tuple items then we can use this items() method.


# items() method in dict{} wit k,v help for loop
# d = {1:10, 2:20, 3:30, 4:40}
# for k,v in d.items():
#     print('Keys:',k,'---','Values:',v)


# update() method in dict{}
# d = {'name':'sai kumar','age':28}
# d1 = {'city':'bangalore','age':28}
# d1 = {'city':'bangalore','age':29}     # it will update with new value
# d.update(d1)    # it will update with new value
# print(d)        # output = {'name': 'sai kumar', 'age': 28, 'city': 'bangalore'}


# is it possible to allow list,tuple,set values in dictonary?
# d_list = {'name':'sai kumar',[1,2]:28}
# d_tuple = {'name':'sai kumar',(1,2):28}
# d_set = {'name':'sai kumar',{1,2}:28}
# d_dict = {'name':'sai kumar',{1:'sai',2:'kumar'}:28}
# print(d_list)       # output = TypeError: unhashable type: 'list'
# print(d_tuple)      # output = {'name': 'sai kumar', (1, 2): 28}
# print(d_set)         # output = TypeError: unhashable type: 'set'
# print(d_dict)          # output = TypeError: unhashable type: 'dict'


# Nested Dictonary:
# =================
# nested_dict = {'outer_key':{'inner_key':'value'}}
# print(nested_dict['outer_key']['inner_key'])                 #getting dict value     # output = value

# nested_dict['outer_key']['new_inner_key'] = 'new_value'       #updating    # output = {'outer_key': {'inner_key': 'value', 'new_inner_key': 'new_value'}}
# print(nested_dict)

# del nested_dict['outer_key']['inner_key']                       #deleting   # output = {'outer_key': {}}
# print(nested_dict)


# for loop in Nested Dictonary?
# nested_dict = {'outer_key':{'inner_key':'value','inner_key2':'inner_value2'}}
# for outer_key, inner_dict in nested_dict.items():
#     print('Outer_key:',outer_key)
#     for inner_key, value in inner_dict.items():
#         print('Inner_key:',inner_key,'<-->','Value:',value)


# How to find Sum() method in dict{}?
# d = {1:10, 2:20, 3:30, 4:40, 5:50}
# print('Sum of of Keys:',sum(d.keys()))          # output = 15
# print('Sum of of Values:',sum(d.values()))      # output = 150
# print(d.items())                                # output = dict_items([(1, 10), (2, 20), (3, 30), (4, 40), (5, 50)])


# Program to find a Occerences each character in Python?
# str = input('Enter a word to find Occurences of each character:')
# d = {}
# for x in str:
#     d[x] = d.get(x,0)+1
# for k,v in d.items():
#     print(k, 'occured in',v,'times')


# Dictonary Comprehension:
# ========================
# syntax:
# dict_c = {expression iteration condition}

# for loop using in dict_c?
dict_c = {x for x in range(1,11)}
print(dict_c)                                                       # output = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# Ex: to Find Square values by using dict_comprehension?
dict_c = {x:x**2 for x in range(1,5)}
print(dict_c)                                                       # output = {1: 1, 2: 4, 3: 9, 4: 16}

# by using list How to Find Quebe by using dict_comprehension?
l = [1,2,3,4,5]
dict_c = {x:x**3 for x in l}
print(dict_c)                                                       # output = {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}

# by using tuple How to Find Quebe by using dict_comprehension?
t = (1,2,3,4,5)
dict_c = {x:x**2 for x in t}
print(dict_c)                                                       # output = {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}

# by using set How to Find Quebe by using dict_comprehension?
s = [1,2,3,4,5]
dict_c = {x:x**2 for x in s}
print(dict_c)                                                       # output = {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}