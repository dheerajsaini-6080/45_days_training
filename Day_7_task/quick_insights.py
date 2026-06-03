"""
Q7: describe() and value_counts()
"""

import pandas as pd

df = pd.read_csv("sample_data.csv")

print("Describe")
print(df.describe())

print("\nValue Counts")
print(df["Age"].value_counts())

print("\nObservation:")
print("Highest marks are above average.")