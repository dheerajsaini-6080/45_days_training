# CSV Student Records
# Creates students.csv, calculates averages, and generates results.csv.

import csv

students_data = [
    ["Dheeraj", 90, 85, 88],
    ["Rahul", 75, 80, 78],
    ["Priya", 95, 92, 96]
]

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["name", "math", "science", "english"])

    writer.writerows(students_data)

print("students.csv created successfully.")

results = []

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        avg = (
            int(row["math"]) +
            int(row["science"]) +
            int(row["english"])
        ) / 3

        if avg >= 90:
            grade = "A"
        elif avg >= 80:
            grade = "B"
        elif avg >= 70:
            grade = "C"
        elif avg >= 60:
            grade = "D"
        else:
            grade = "F"

        results.append({
            "name": row["name"],
            "average": round(avg, 2),
            "grade": grade
        })

with open("results.csv", "w", newline="") as file:
    fieldnames = ["name", "average", "grade"]

    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()

    writer.writerows(results)

print("results.csv generated successfully.")

