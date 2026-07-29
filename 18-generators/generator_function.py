"""
Generator Function

This example demonstrates a generator function.
"""


def numbers():

    yield 1
    yield 2
    yield 3


generator = numbers()

print(next(generator))
print(next(generator))
print(next(generator))