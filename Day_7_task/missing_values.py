"""
Q6: Missing Values
"""

import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Name": ["A", "B", "C"],
    "Marks": [80, np.nan, 90]
})

print("Missing Values")
print(df.isnull().sum())

print("\nUsing fillna")
print(df.fillna(0))

print("\nUsing dropna")
print(df.dropna())