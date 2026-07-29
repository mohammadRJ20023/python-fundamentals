"""
Class Attributes

This example demonstrates class attributes.
"""


class Person:

    species = "Human"

    def __init__(self, name):

        self.name = name


person1 = Person("MohammadReza")
person2 = Person("Ali")

print(person1.species)
print(person2.species)
