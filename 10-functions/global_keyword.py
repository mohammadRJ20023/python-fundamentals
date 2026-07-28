"""
Global Keyword

This example demonstrates the global keyword.
"""

counter = 0


def increment():
    global counter

    counter += 1


increment()
increment()

print(counter)