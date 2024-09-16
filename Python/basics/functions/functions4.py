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
def generate_square_normal(n):
    square = []
    for i in range(n):
        square.append(i**2)
    return square
result_normal = generate_square_normal(5)
print(result_normal)

# Square of Each Number in a Given Numbers in Generator Function
def generate_square_generator_function(n):
    for i in range(n):
        yield i**2
result_gen = generate_square_generator_function(10)
print(next(result_gen))
