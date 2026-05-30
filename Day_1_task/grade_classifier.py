# This program classifies students based on marks.

students = [
    {"name": "Aman", "score": 95},
    {"name": "Riya", "score": 82},
    {"name": "Rahul", "score": 74},
    {"name": "Sneha", "score": 61},
    {"name": "Kunal", "score": 40}
]

def classify(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 50:
        return "D"
    else:
        return "F"

sorted_students = sorted(
    students,
    key=lambda student: student["score"],
    reverse=True
)

for student in sorted_students:
    grade = classify(student["score"])

    print(
        f"{student['name']} scored {student['score']} and got Grade {grade}"
    )