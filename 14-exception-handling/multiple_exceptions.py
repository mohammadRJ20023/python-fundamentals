"""
Multiple Exceptions

This example demonstrates handling multiple exceptions.
"""

try:

    number = int(input("Enter a number: "))

    result = 10 / number

    print(result)

except ValueError:

    print("Invalid number.")

except ZeroDivisionError:

    print("Cannot divide by zero.")