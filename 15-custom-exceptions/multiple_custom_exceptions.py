"""
Multiple Custom Exceptions

This example demonstrates using multiple custom exceptions.
"""


class InvalidAgeError(Exception):
    pass


class InvalidUsernameError(Exception):
    pass


username = ""
age = -2


if not username:
    raise InvalidUsernameError("Username cannot be empty.")

if age < 0:
    raise InvalidAgeError("Age cannot be negative.")