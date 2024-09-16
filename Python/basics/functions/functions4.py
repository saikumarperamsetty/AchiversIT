# Generator Function
# def mygen():
#     yield 'A'
#     yield 'B'
#     yield 'C'
# g = mygen()
# print(g)  #it will give object information
# print(next(g))  #it will print Yield value of "A"
# print(next(g))  #it will print Yield value of "B"
# print(next(g))  #it will print Yield value of "C"
# print(next(g))  #it will give stopIteration error

# Square of Each Number in a Given Numbers in Normal Function
# def generate_square_normal(n):
#     square = []
#     for i in range(n):
#         square.append(i**2)
#     return square
# result_normal = generate_square_normal(5)
# print(result_normal)

# # Square of Each Number in a Given Numbers in Generator Function
# def generate_square_generator_function(n):
#     for i in range(n):
#         yield i**2
# result_gen = generate_square_normal(10)
# print(result_gen)

# How to Create Coundown Function by using generator function
# def countdown(num):
#     print('coundown starts:')
#     while num > 0:
#         yield num
#         num = num-1
# value = countdown(10)
# for i in value:
#     print(i)

# Fibonacci Number using generator Function
def fibinacci():
    a,b = 0,1
    while True:
        yield a
        a,b=b,a+b
for i in fibinacci():
    if i >150:
        break
    print(i)