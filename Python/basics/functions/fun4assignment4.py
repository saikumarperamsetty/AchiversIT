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
def infinite_sequence():
    a = 0
    while True:
        a +=1
        yield a
for i in infinite_sequence():
    if i >= 21:
        break
    print(i)