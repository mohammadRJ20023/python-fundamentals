"""
Inheritance

This example demonstrates inheritance.
"""


class Animal:

    def speak(self):

        print("Animal sound")


class Dog(Animal):

    pass


dog = Dog()

dog.speak()
