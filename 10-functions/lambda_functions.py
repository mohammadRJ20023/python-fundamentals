"""
Lambda Functions

This example demonstrates lambda functions.
"""



# Lambda with multiple arguments
add_with_lambda = lambda a, b: a + b

def simple_add_func(a,b):
    return a + b


print(f"with lambda = {add_with_lambda(10, 20)}")
print(f"simple func = {simple_add_func(10, 20)}")

# Create a lambda function
square = lambda number: number ** 2

print(square(5))

