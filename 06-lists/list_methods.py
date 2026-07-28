"""
List Methods

This example demonstrates common list methods.
"""

numbers = [10, 20, 30]

numbers.append(40)
print(f"append 40 = {numbers}")

numbers.insert(1, 15)
print(f"insert = {numbers}")

numbers.remove(20)
print(f"remove 20 = {numbers}")

numbers.pop()
print(f"pop = {numbers}")

print(numbers)