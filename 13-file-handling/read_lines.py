"""
Read Lines

This example demonstrates reading a file line by line.
"""

with open("sample.txt", "r") as file:

    # Read all lines as a list
    lines = file.readlines()

for line in lines:
    print(line.strip())