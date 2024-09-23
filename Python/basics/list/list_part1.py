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
# l = []
# l.append('PERAMSETTY')
# l.append('SAI')
# l.append('KUMAR')
# l.append(28)
# print(l)
# print(type(l))

# # Ex:2 If we Know list values in Advance?
# # Type-2:
# l = [10,20,30,40,50]
# print(l)
# print(type(l))


# # Ex:3 by splitting the String values?
# # Type-3:
# str = 'Learning Python is Very Easy'
# s = str.split()
# print(s)
# print(type(s))


# # Ex:4 by using list function?
# # Type-4:
# l = list([28,30,29])
# print(l)
# print(type(l))


# # Ex:5 by using eval function?
# # Type-5:
# l = eval(input('Enter list values(by using eval):'))
# print(l)
# print(type(l))


# Ex:6 How to use indexing in list?
# l = [10,20,30,40,50]
# print(l[3])
# print(l[1])
# print(l[-1])


# Ex:7 How to use slicing in list?
# slice = [start:end:step]
# l = [10,20,30,40,50,28,21,14,92,24,67]
# sliced = l[4:-3]
# print(sliced)


# Ex:8 How to use Traversing in list?
# l = [10,22,35,48,55,28,21,11,92,25,67]

# # printing values by using for loop
# for i in l:
#     print(i)

# # printing values by using while loop
# i = 0
# while i < len(l):
#     print(l[i])
#     i += 1

# # # for Even numbers
# for i in l:
#     if i % 2 == 0:
#         print(i)

# # # for odd numbers
# for i in l:
#     if i % 2 != 0:
#         print(i)


# Ex:9 How apply len() method in list?
l = [28,98,41,84,32,19,24,52,47,23]
print(len(l))     # output = 10

# Ex:10 How apply count() method in list?
l = [28,98,41,84,32,19,28,52,47,28]
print(l.count(28))    # output = 3

# Ex:11 How apply index() method in list?
l = [28,98,41,84,32,19,24,52,47,23]
print(l.index(19))      # output = 5

# Ex:12 How apply pop() method in list?
l = [28,98,41,84,32,19,24,52,47,23]
print(l.pop())      # output = 23