# Ex:1. Basic Decorator Function:
# Write a decorator that prints "Hello" before executing a function and 
# "Goodbye" after executing it. 
# Apply this decorator to a function that prints "World"?
# def before_decorator(before_decorator):
#     def inner(*args,**kwargs):
#             print('Hello')
#             before_decorator()
#             print('GoodBye')
#     return inner

# @before_decorator
# def after_decorator():
#       print('World')
# after_decorator()


# Ex:2. Timing Function Execution:
# Create a decorator that measures the time a function takes to execute. 
# Apply this decorator to a function that sums numbers from 1 to 1,000,000.?
# import time
# # Decorator to measure execution time
# def time_it(func):
#     def wrapper(*args,**kwargs):
#         start_time = time.time()     # Start time
#         result = func(*args,**kwargs)      # Call the function
#         end_time = time.time()       # End time
#         elapsed_time = end_time - start_time    # Calculate elapsed time
#         print(f'Execution Time:{elapsed_time:.6f} seconds')
#         return result   # Return the function result
#     return wrapper

# # Function to sum numbers from 1 to 1,000,000
# @time_it
# def sum_of_numbers(n):
#     return sum(range(1,n+1))

# # Call the function
# result = sum_of_numbers(1_00_000)
# print(f'Sum of Numbers from 1 to 100000: {result}')


# 3. Repeat Execution: 
# Write a decorator that executes a function three times. Test this decorator on a function that prints a given message?

# Decorator to execute a function three times
# def execute_three_times(func):
#     def wrapper(*args,**kwargs):
#           for _ in range(3):
#             func(*args,**kwargs)
#     return wrapper

# # Function to print a message
# @execute_three_times
# def print_message(message):
#     print(message)

# # Call the function
# print_message('Hello, this message will be printed three(3) times!')


# 4. Access Control Decorator: 
# Create a decorator that checks if a user is an admin before allowing the execution of a function. If the user is not an admin, print "Access Denied". Test with a simple function that returns a protected message?

# Decorator to check if a user is an admin
# def admin_requied(func):
#     def wrapper(user):
#         if user.get('is_admin'):
#             return func(user)  # Call the function if the user is admin
#         else:
#             print('Access Denied..')      # Print message if not admin
#     return wrapper

# # Function to return a protected message
# @admin_requied
# def protected_message(user):
#     return'This is Protected, for Admins only'

# # Test with an admin user
# admin_user = {'name':'sai','is_admin':True}
# print(protected_message(admin_user))       # Should print the protected message

# # Test with a non-admin user
# non_admin_user = {'name':'suraj','is_admin':False}
# print(protected_message(non_admin_user))  # Should print "Access Denied"


# 5. Decorator with Arguments: 
# Write a decorator that accepts a string argument and prints it before executing the function. Apply it to a function that returns a greeting message?

# Decorator that accepts a string argument
def print_message(message):
    def decorator(func):
        def wrapper(*args,**kwargs):
            print(message)  # Print the message before executing the function
            return func(*args,**kwargs) # Call the original function
        return wrapper
    return decorator

# Function to return a greeting message
@print_message("Executing the greeting function...")
def greet(name):
    return f'Hi Mr.{name}!'

# Call the function
result = greet('PERAMSETTY SAI KUMAR')
print(result)