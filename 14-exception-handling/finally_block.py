"""
Finally Block

This example demonstrates the finally block.
"""

try:

    file = open("sample.txt", "r")

    print(file.read())

except FileNotFoundError:

    print("File not found.")

finally:

    print("Program finished.")