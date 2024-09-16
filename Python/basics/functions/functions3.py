# Decorator Function Working
# def decor(wish):
#     def inner(name):
#         if name == 'Sai':
#             print('Hi',name,'Good Morning! Have Great Day..')
#         else:
#             wish(name)
#     return inner
# @decor
# def wish(name):
#     print('Hello',name,'Good Morning')
# wish('Suraj')
# wish('Sai')
# wish('Madhavi')

# Ex:1
# def outer_function(func):
#     def inner_func(a,b):
#         print('we are going to devide',a,'by',b)
#         if b == 0:
#             print('division by zeo! How is it possible Deviding by 0')
#             return
#         else:
#             return (func(a,b))
#     return inner_func
# @outer_function
# def smart_division(a,b):
#     return a/b
# result = smart_division(28,2)
# print(result)
# result = smart_division(28,0)
# print(result)

# Ex:2
# Decorator Chaining
def decor_chain2(func):
    def inner():
        x = func()
        return x * x
    return inner
    
def decor_chain1(func):
    def inner():
        x = func()
        return x * 2
    return inner

@decor_chain2
@decor_chain1
def num():
    return 10
result = num()
print(result)