"""
Try Except

This example demonstrates basic exception handling.
"""

try:

    number = int(input("Enter a number: "))

    print(number)

except ValueError:

    print("Invalid input.")