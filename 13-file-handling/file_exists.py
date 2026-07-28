"""
File Exists

This example demonstrates checking whether a file exists.
"""

import os

filename = "sample.txt"

# Check if the file exists
if os.path.exists(filename):
    print("File exists.")
else:
    print("File not found.")