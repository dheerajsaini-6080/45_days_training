"""
Q5: loc vs iloc
"""

import pandas as pd

df = pd.read_csv("sample_data.csv")

print("LOC Example")
print(df.loc[0:2, ["Name", "Marks"]])

print("\nILOC Example")
print(df.iloc[0:3, [0, 2]])

print("\nloc = label based")
print("iloc = position based")