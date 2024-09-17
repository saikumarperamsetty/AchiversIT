# 1. Write a generator function that yields the Fibonacci sequence up to a 
# given number n. Test the generator by printing the first 10 numbers in 
# the sequence.
# FIBONACCI SERIES UPTO GIVEN n?
# def fibonacci_series():
#     a,b = 0,1
#     while True:
#         yield a
#         a,b = b, a+b
# for i in fibonacci_series():
#     if i > 50:
#         break
#     print(i)


# 2. Create a generator that yields an infinite sequence of natural numbers 
# starting from 1. Use next() to print the first 20 numbers.
# def infinite_sequence():
#     a = 0
#     while True:
#         a +=1
#         yield a
# for i in infinite_sequence():
#     if i >= 21:
#         break
#     print(i)


# 3. Write a generator that yields prime numbers up to a given limit. 
# Implement the Sieve of Eratosthenes algorithm to optimize the 
# generator.
from math import isqrt
def primes_less_sieve_of_erostothenses(n:int)->list[int]:
    if n <= 2:
        return []
    
    is_prime = [True] * n
    is_prime[0] = False
    is_prime[1] = False

    for i in range(2, isqrt(n)):
        if is_prime[i]:
            for x in range(i*i, n, i):
                is_prime[x] = False
    return [i for i in range(n) if is_prime[i]]

if __name__ == '__main__':
    print(primes_less_sieve_of_erostothenses(100))