"""
Variable Scope

This example demonstrates local and global variables.
"""

message = "Global"

def show_message():
    message = "Local"
    print(message)

show_message()

print(message)