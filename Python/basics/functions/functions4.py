# Generator Function
def mygen():
    yield 'A'
    yield 'B'
    yield 'C'
g = mygen()
# print(g)  #it will give object information
print(next(g))  #it will print Yield value of "A"
print(next(g))  #it will print Yield value of "B"
print(next(g))  #it will print Yield value of "C"
print(next(g))  #it will give stopIteration error