"""
Custom Exception

This example demonstrates how to create a custom exception.
"""


class InvalidAgeError(Exception):
    pass


age = -10

if age < 0:
    raise InvalidAgeError("Age cannot be negative.")