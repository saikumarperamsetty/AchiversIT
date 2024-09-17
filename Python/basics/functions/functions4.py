# Ex:1 Generator Function
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

# Ex:2 Square of Each Number in a Given Numbers in Normal Function
# def generate_square_normal(n):
#     square = []
#     for i in range(n):
#         square.append(i**2)
#     return square
# result_normal = generate_square_normal(5)
# print(result_normal)

# # Ex:3 Square of Each Number in a Given Numbers in Generator Function
# def generate_square_generator_function(n):
#     for i in range(n):
#         yield i**2
# result_gen = generate_square_normal(10)
# print(result_gen)

# Ex:4 How to Create Coundown Function by using generator function
# def countdown(num):
#     print('coundown starts:')
#     while num > 0:
#         yield num
#         num = num-1
# value = countdown(10)
# for i in value:
#     print(i)

# Ex:5 Fibonacci Number using generator Function
# def fibinacci():
#     a,b = 0,1
#     while True:
#         yield a
#         a,b=b,a+b
# for i in fibinacci():
#     if i >100:
#         break
#     print(i)


# Ex:6 Write a generator that yields prime numbers up to a given limit. with the help of Sieve of Eratosthenes algorithm?
from math import isqrt
def prime_less_Sieve_Of_Erostothenes(n:int)-> list[int]:
    if n <= 2:
        return []
    is_prime = [True] * n
    is_prime[0] = False
    is_prime[1] = False

    for i in range(2, isqrt(n)):
        if is_prime[i]:
            for x in range(i*i, n, i):
                is_prime[x] = False
    return [i for i in range(x) if is_prime[i]]
if __name__ == '__main__':
    print(prime_less_Sieve_Of_Erostothenes(100))