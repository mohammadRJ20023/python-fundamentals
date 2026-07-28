"""
Recursion

This example demonstrates recursion in Python.
"""

# Calculate factorial using recursion
def factorial(number):
    if number == 1:
        return 1

    return number * factorial(number - 1)


print(factorial(5))