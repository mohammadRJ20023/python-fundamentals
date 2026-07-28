"""
Mini Project

Password Generator
"""

import random

characters = (
    "abcdefghijklmnopqrstuvwxyz"
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    "0123456789"
    "!@#$%^&*"
)
#or characters = ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*")

password = ""

# Generate a 12-character password
for _ in range(12):
    password += random.choice(characters)

print(password)