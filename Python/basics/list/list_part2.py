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


# Ex:29 How to Find Even & Odd Numbers Sum on list in Python?
l = [1,2,3,4,5,6,7,8,9]
even_sum = 0
odd_sum = 0
for num in l:
    if num % 2 == 0:
        even_sum += num
    else:
        odd_sum += num
print('Even Numbers Sum in Given List: ',even_sum)
print('Odd Numbers Sum in Given List: ',odd_sum)