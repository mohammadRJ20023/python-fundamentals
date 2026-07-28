"""
Dictionary Methods

This example demonstrates common dictionary methods.
"""

user = {
    "name": "Mohammadreza",
    "age": 23
}

user["city"] = "Shiraz"
user.update({"country": "Iran"})

print(user)

user.pop("age")

print(user)

print(user.keys())
print(user.values())
print(user.items())