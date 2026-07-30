"""
**kwargs

This example demonstrates **kwargs.
"""

def information(**data):

    for key, value in data.items():

        print(f"{key}: {value}")


information(name="MohammadReza", age=22)