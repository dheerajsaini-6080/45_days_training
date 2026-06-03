"""
Q9: Masking, Broadcasting and Cosine Similarity
"""

import numpy as np


def cosine_similarity(v1, v2):
    return np.dot(v1, v2) / (
        np.linalg.norm(v1) * np.linalg.norm(v2)
    )


arr = np.array([10, 20, 30, 40, 50])

mask = arr > 25

print("Mask:")
print(arr[mask])

print("\nBroadcasting:")
print(arr + 10)

v1 = np.array([1, 2, 3])
v2 = np.array([1, 2, 3])

v3 = np.array([4, 5, 6])

print("\nSimilarity 1:")
print(cosine_similarity(v1, v2))

print("\nSimilarity 2:")
print(cosine_similarity(v1, v3))