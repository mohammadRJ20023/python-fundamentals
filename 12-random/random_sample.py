"""
Random Sample

This example demonstrates random sampling.
"""

import random

numbers = list(range(1, 21))

# Select unique random values
sample = random.sample(numbers, 5)

print(sample)