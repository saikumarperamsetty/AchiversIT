# 1. Write a generator function that yields the Fibonacci sequence up to a 
# given number n. Test the generator by printing the first 10 numbers in 
# the sequence.
# FIBONACCI SERIES UPTO GIVEN n?
def fibonacci_series():
    a,b = 0,1
    while True:
        yield a
        a,b = b, a+b
for i in fibonacci_series():
    if i > 50:
        break
    print(i)