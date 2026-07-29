"""
Yield

This example demonstrates the yield keyword.
"""


def countdown(number):

    while number > 0:

        yield number

        number -= 1


for value in countdown(5):

    print(value)