"""
Sort Objects

This example demonstrates sorting objects.
"""


class Student:

    def __init__(self, name, score):

        self.name = name
        self.score = score


students = [
    Student("Ali", 18),
    Student("Sara", 20),
    Student("Reza", 15),
]

students.sort(key=lambda student: student.score)

for student in students:

    print(student.name, student.score)