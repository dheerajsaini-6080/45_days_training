"""
Q8: NumPy Array Creation and Slicing
"""

import numpy as np

a = np.array([10, 20, 30, 40, 50])

b = np.arange(1, 11)

print(a)
print("Shape:", a.shape)
print("Dtype:", a.dtype)
print("Dimensions:", a.ndim)

print("\nLast Element:", a[-1])

print("Slice:", b[2:7])