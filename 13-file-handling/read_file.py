"""
Read File

This example demonstrates how to read a text file.
"""

# Open the file in read mode
file = open("sample.txt", "r")

# Read the entire file
content = file.read()

print(content)

# Close the file
file.close()
