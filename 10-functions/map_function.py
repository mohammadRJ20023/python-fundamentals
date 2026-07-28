"""
Map Function

This example demonstrates the map() function.
"""

numbers = [1, 2, 3, 4, 5]

# Apply a function to each item
squared_numbers = list(map(lambda number: number ** 2, numbers))

print(squared_numbers)

# Convert strings to uppercase
names = ["ali", "sara", "mohammad"]

uppercase_names = list(map(str.upper, names))

print(uppercase_names)