"""
Random Choice

This example demonstrates random selection.
"""

import random

fruits = ["Apple", "Banana", "Orange", "Mango"]

# Select a random item
print(random.choice(fruits))

# Select multiple random items
print(random.choices(fruits, k=3))