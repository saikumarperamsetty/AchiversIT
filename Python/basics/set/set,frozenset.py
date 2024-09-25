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
s = set()
s.add(28)                   # it will add only one item at a time
s.add((10,28,30,40,50))     # it will add only one item at a time
print(s)                    #  output = {28, (10, 28, 30, 40, 50)}

# How to update elements in set{}?
s = set()
l = [10,28,30,40,50]
s.update(l,range(1,6))    # it is updating with range function along with that values 1,2,3,4,5
s.update(l,range(1,11))    # it is updating Function will take the collection of values only
s.add('SAI KUMAR')        # it is adding the string value to set'SAI KUMAR'
print(s)                  #  output = {1, 2, 3, 4, 5, 40, 10, 'SAI KUMAR', 50, 28, 30}

# copy() method in set?
s = {10,28,30,40,50}
copied_set = s.copy()
print(id(copied_set))
print(id(s))