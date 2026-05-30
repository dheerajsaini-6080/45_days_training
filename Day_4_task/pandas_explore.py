# Pandas Dataset Exploration
# Demonstrates DataFrame operations.

import pandas as pd

data = {
    "name": [
        "A", "B", "C", "D", "E",
        "F", "G", "H", "I", "J"
    ],
    "city": [
        "Jaipur", "Delhi", "Jaipur",
        "Mumbai", "Delhi",
        "Mumbai", "Jaipur",
        "Delhi", "Mumbai", "Jaipur"
    ],
    "math_score": [90, 75, 88, 70, 85, 95, 60, 78, 82, 91],
    "science_score": [85, 80, 90, 75, 88, 92, 65, 79, 81, 89],
    "english_score": [80, 82, 87, 72, 84, 91, 68, 77, 83, 90]
}

df = pd.DataFrame(data)

print("Average Scores")
print(df[["math_score", "science_score", "english_score"]].mean())

df["total"] = (
    df["math_score"]
    + df["science_score"]
    + df["english_score"]
)

print("\nHighest Total Score")
print(df.loc[df["total"].idxmax()])

print("\nStudents per City")
print(df.groupby("city").size())

print("\nMath Score > 75")
print(df[df["math_score"] > 75])

print("\nTop 3 Students")
print(df.nlargest(3, "total"))