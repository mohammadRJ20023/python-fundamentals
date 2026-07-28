"""
Random Seed

This example demonstrates reproducible random values.
"""

import random

# Set a fixed seed
random.seed(42)

print(random.randint(1, 100))
print(random.randint(1, 100))