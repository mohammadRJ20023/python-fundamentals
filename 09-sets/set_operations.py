"""
Set Operations

This example demonstrates common set operations.
"""

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Combine all unique elements from both sets
print(set_a.union(set_b))

# Return common elements between both sets
print(set_a.intersection(set_b))

# Return elements that exist only in set_a
print(set_a.difference(set_b))

# Return elements that are not shared between the sets
print(set_a.symmetric_difference(set_b))