"""
With Statement

This example demonstrates using the with statement.
"""

# The file closes automatically
with open("sample.txt", "r") as file:
    print(file.read())