"""
Variable-Length Arguments

This example demonstrates *args.
"""

def total(*numbers):
    print(sum(numbers))

# Pass multiple values
total(10, 20, 30, 40)