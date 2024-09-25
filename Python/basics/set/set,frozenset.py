# Set{} Datatype:

#Ex:1 How to create a set in Python?
# by using set() function?
# s = set((1,2,3,4,5))
# print(s)
# print(type(s))

# # by using set() function How to convert ?
# s = set([1,2,3,4,5])
# print(s)
# print(type(s))

# # by using set{} datatype to create a set?
# s = {1,2,3,4,5}
# print(s)
# print(type(s))

# Functions on set{}
# How to add elements in set{}?
# s = set()
# s.add(28)                   # it will add only one item at a time
# s.add((10,28,30,40,50))     # it will add only one item at a time
# print(s)                    #  output = {28, (10, 28, 30, 40, 50)}

#Ex:2 How to update elements in set{}?
# s = set()
# l = [10,28,30,40,50]
# s.update(l,range(1,6))    # it is updating with range function along with that values 1,2,3,4,5
# s.update(l,range(1,11))    # it is updating Function will take the collection of values only
# s.add('SAI KUMAR')        # it is adding the string value to set'SAI KUMAR'
# print(s)                  #  output = {1, 2, 3, 4, 5, 40, 10, 'SAI KUMAR', 50, 28, 30}

# copy() method in set?
# s = {10,28,30,40,50}
# copied_set = s.copy()
# print(id(copied_set))
# print(id(s))

# pop() method in set?
# s = {10,28,30,40,50,65}
# set_pop = s.pop()           # it will remove the last element in the set
# print(s)                    # output = {50, 40, 10, 28, 30}

# remove() method in set?
# s = {10,28,30,40,50,65}
# s.remove(40)                # it will remove that particular element in the set
# print(s)                    # output = {65, 50, 10, 28, 30}

# discard() method in set?
# s = {10,28,30,40,50,65}
# s.discard(50)               # it will discard that particular element in the set
# s.discard(90)               # it will not giving the error in the set
# print(s)                    # output = {65, 40, 10, 28, 30}

# clear() method in set?
# s = {10,28,30,40,50,65}
# s.clear()                   # it will clear the total elements in the set
# print(s)                    # output = it is giving empty as result i.e set()


#Ex:3 Mathematical Functions on Set{} Datatype:
# union(): --> |
# intersection(): --> &
# difference(): --> -
# symmetric_diffrence(): --> ^
# isdisjoint():
# issuperset():
# issubset():

# How to use union() method in set?
# x = {10,20,30,40}
# y = {30,40,50,60}
# print(x.union(y))       # it will check common elements without duplicates
# print(x|y)              # output = {40, 10, 50, 20, 60, 30}

# How to use intersection() method in set?
# x = {10,20,30,40}
# y = {30,40,50,60}
# print(x.intersection(y))    # it will check only common elements from both sets
# print(x&y)                  # output = {40,30}

# How to use difference() method in set?
# x = {10,20,30,40}
# y = {30,40,50,60}
# print(x.difference(y))          # it will check only unique elements w.r.t x-y or y-x from both sets
# print(x-y)                      # output = {10, 20}

# How to use symmetric_diffrence() method in set?
# x = {10,20,30,40}
# y = {30,40,50,60}
# print(x.symmetric_difference(y))    # it will check only other than common elements rest of the elements from both sets
# print(x^y)                          # output = {10, 50, 20, 60}

# How to use isdisjoint() method in set?
# x = {10,20,30,40}
# y = {30,40,50,60}
# print(x.isdisjoint(y))    #False          # check if common elements are connected from both sets, then it will False

# How to use issubset() method in set?
# x = {10,20,30,40}
# y = {30,40,50,60}
# print(x.issubset(y))     #False            # check if all x (or) y set elements are connected in y (or) x set elements or not, if all elements are connected then it will give True

# How to use issuperset() method in set?
# x = {10,20,30,40}
# y = {10,20,30,40,50,60,70,80}
# print(x.issuperset(y))   #False              # check if all x (or) y set elements are connected in y (or) x set elements or not, if all elements are connected then it will give True
# print(y.issuperset(x))   #True


#Ex:4 Realtime Example of set{} datatype with integer values?
# student_ids = [101,102,103,104,105,106,107,108,109,11171,218,28]
# unique_set = set()
# for id in student_ids:
#     unique_set.add(id)
#     print('Unique Set Ids: ',unique_set)

# print('is 108 in the set? ',108 in unique_set)
# print('is 11171 in the set? ',11171 in unique_set)
# print('is 228 in the set? ',28 in unique_set)
# print('is 218 in the set? ',218 in unique_set)
# print('is 254 in the set? ',254 in unique_set)


#Ex:5 Realtime Example of set{} datatype with String values?
# str1 = {'MySQL','Bhagavdhgita','Khurran','Bible','Java','Python'}
# str2 = {'React','JavaScript','Bhagavdhgita','Khurran','Bible','Ramayana','Mahabharata'}
# print(str1.union(str2))
# print(str1.intersection(str2))
# print(str1.difference(str2))
# print(str1.symmetric_difference(str2))
# print(str1.isdisjoint(str2))
# print(str1.issubset(str2))
# print(str2.issuperset(str1))


# set comprehension: it means compact way (or) shorter way to create set.
# syntax = {expression iteration condition}
# set_c = {x for x in range(1,11) if x % 3 == 0}
# print(set_c)


# FrozenSet Datatype:
# It is immutable version of set{} datatype
l = [10,20,30]
f = frozenset(l)
print(f)            # output = frozenset({10, 20, 30})

# for loop in frozenset{}
l = [10,20,30]
f = frozenset(l)
for x in f:
    print(x)            # output = 10 20 30

# max() method in frozenset{}
l = [10,20,30]
f = frozenset(l)
print(max(f))           # output = 30

# min() method in frozenset{}
l = [10,20,30]
f = frozenset(l)
print(min(f))           # output = 10

# sum() method in frozenset{}
l = [10,20,30]
f = frozenset(l)
print(sum(f))           # output = 60