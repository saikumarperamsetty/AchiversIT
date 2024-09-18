# Ex:1. Basic Decorator Function:
# Write a decorator that prints "Hello" before executing a function and 
# "Goodbye" after executing it. 
# Apply this decorator to a function that prints "World"?
def before_decorator(before_decorator):
    def inner(*args,**kwargs):
            print('Hello')
            before_decorator()
            print('GoodBye')
    return inner

@before_decorator
def after_decorator():
      print('World')
after_decorator()


# Ex:2. Timing Function Execution:
# Create a decorator that measures the time a function takes to execute. 
# Apply this decorator to a function that sums numbers from 1 to 1,000,000.?
import time
# Decorator to measure execution time
def time_it(func):
    def wrapper(*args,**kwargs):
        start_time = time.time()     # Start time
        result = func(*args,**kwargs)      # Call the function
        end_time = time.time()       # End time
        elapsed_time = end_time - start_time    # Calculate elapsed time
        print(f'Execution Time:{elapsed_time:.6f} seconds')
        return result   # Return the function result
    return wrapper

# Function to sum numbers from 1 to 1,000,000
@time_it
def sum_of_numbers(n):
    return sum(range(1,n+1))

# Call the function
result = sum_of_numbers(1_00_000)
print(f'Sum of Numbers from 1 to 100000: {result}')