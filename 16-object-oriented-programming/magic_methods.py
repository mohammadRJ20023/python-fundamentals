"""
Magic Methods

This example demonstrates the __str__ magic method.
"""


class Person:

    def __init__(self, name):

        self.name = name

    def __str__(self):

        return self.name


person = Person("MohammadReza")

print(person)