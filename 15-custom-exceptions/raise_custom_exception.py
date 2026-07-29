"""
Raise Custom Exception

This example demonstrates handling a custom exception.
"""


class InvalidAgeError(Exception):
    pass


try:

    age = -5

    if age < 0:
        raise InvalidAgeError("Age cannot be negative.")

except InvalidAgeError as error:

    print(error)