"""
List Comprehensions

This example demonstrates how to create lists using list comprehensions.
"""

numbers = [1, 2, 3, 4, 5]

# Create a new list with squared numbers
squared_numbers = [number ** 2 for number in numbers]

print(squared_numbers)

# Create a list of even numbers
even_numbers = [number for number in numbers if number % 2 == 0]

print(even_numbers)

# Convert names to uppercase
names = ["ali", "sara", "mohammad"]

uppercase_names = [name.upper() for name in names]

print(uppercase_names)