"""
Custom Iterator

This example demonstrates a custom iterator.
"""


class Counter:

    def __init__(self):

        self.number = 1

    def __iter__(self):

        return self

    def __next__(self):

        if self.number > 5:
            raise StopIteration

        value = self.number

        self.number += 1

        return value


counter = Counter()

for number in counter:

    print(number)