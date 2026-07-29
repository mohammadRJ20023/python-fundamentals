"""
Generator Expression

This example demonstrates a generator expression.
"""

numbers = (number * number for number in range(1, 6))

for number in numbers:

    print(number)