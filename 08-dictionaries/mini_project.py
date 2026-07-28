"""
Mini Project

Student Profile
"""

student = {
    "name": "Mohammadreza",
    "age": 23,
    "major": "Computer Engineering",
    "city": "Shiraz"
}

print("Student Information")

for key, value in student.items():
    print(f"{key}: {value}")