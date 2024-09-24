# Ex:27 Membership operators on list in Python?
#  Membership operators = in, not in
# l = [10,30,20,90,40,50]
# print(90 in l)          # output = True
# print(180 in l)         # output = False
# print(60 not in l)      # output = True
# print(30 not in l)      # output = False


# Ex:28 max(), min() and sum() methods on list in Python?
# max()
# l = [10,90,40,50,30]
# print(max(l))           # output = 90

# # min()
# l = [10,90,40,50,30]
# print(min(l))           # output = 10

# # sum()
# l = [10,20,60,50,40]
# print(sum(l))           # output = 180

# any() and all()
# any()
# l = [True,False,True]
# any_result = any(l)
# all_result = all(l)
# print(any_result)
# print(all_result)

# unpacking(Destructering) in list and tuple
# Destructering = Extracting the items and saving to variable is called 'Destructuring'
# list
# l = [10,20,30]
# a,b,c = l
# print(a)
# print(b)
# print(c)

# tuple
# t = (10,20,30)
# x,y,z = t
# print(x)
# print(y)
# print(z)


# Ex:29 How to Find Even & Odd Numbers Sum on list in Python?
# l = [1,2,3,4,5,6,7,8,9]
# even_sum = 0
# odd_sum = 0
# for num in l:
#     if num % 2 == 0:
#         even_sum += num
#     else:
#         odd_sum += num
# print('Even Numbers Sum in Given List:',even_sum)
# print('Odd Numbers Sum in Given List:',odd_sum)


# Nested Lists:
# Ex:1
# l = [10,20,[30,40],50]
# # for accessing nested list values
# print(l[0])
# print(l[1])
# print(l[3])

# # for accessing inner nested list values
# print(l[2][0])
# print(l[2][1])

# # for updating nested list values
# l[1] = 200
# l[3] = 500
# print(l)

# # for updating inner nested list values
# l[2][0] = 300
# l[2][1] = 400
# print(l)


# Ex:2 Different ways to flatten a Nested list?
l = [[10,20],[30,40],[50,60]]

# flatten list using for loop?
flatten_list = []
for i in l:
    for j in i:
        flatten_list.append(j)
print(flatten_list)

# flatten list using complimentary expression?
flatlist = [y for x in l for y in x]
print(flatlist)

# flatten list using itertools module?
import itertools
flatlistiter = list(itertools.chain.from_iterable(l))
print(flatlistiter)