"""
Append File

This example demonstrates how to append text to a file.
"""

# Open the file in append mode
file = open("sample.txt", "a")

# Add new text to the end of the file
file.write("\nThis line was appended.")

# Close the file
file.close()