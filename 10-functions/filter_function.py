"""
Filter Function

This example demonstrates the filter() function.
"""

numbers = [1, 2, 3, 4, 5, 6]

# Filter even numbers
even_numbers = list(filter(lambda number: number % 2 == 0, numbers))

print(even_numbers)

# Filter numbers greater than 3
greater_than_three = list(filter(lambda number: number > 3, numbers))

print(greater_than_three)