"""
Else Block

This example demonstrates the else block.
"""

try:

    number = int(input("Enter a number: "))

except ValueError:

    print("Invalid input.")

else:

    print(f"Number: {number}")