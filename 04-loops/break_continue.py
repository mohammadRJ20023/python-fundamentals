"""
Break & Continue

This example demonstrates break and continue statements.
"""

for number in range(1, 11):

    if number == 5:
        break

    print(number)

print()

for number in range(1, 11):

    if number % 2 == 0:
        continue

    print(number)