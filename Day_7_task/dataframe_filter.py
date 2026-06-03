"""
Q4: DataFrame Filtering
"""

import pandas as pd

df = pd.read_csv("sample_data.csv")

filtered = df[(df["Marks"] > 80) & (df["Age"] < 21)]

print(filtered[["Name", "Marks"]])