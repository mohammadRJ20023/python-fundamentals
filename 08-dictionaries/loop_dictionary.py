"""
Loop Through Dictionary

This example demonstrates how to iterate through a dictionary.
"""

user = {
    "name": "Mohammadreza",
    "age": 23,
    "city": "Shiraz"
}

for key, value in user.items():
    print(f"{key}: {value}")