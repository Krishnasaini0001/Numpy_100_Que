import numpy as np

arr = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])

print("First two rows:")
print(arr[:2])

print("\nFirst two columns:")
print(arr[:, :2])

print("\nMiddle section:")
print(arr[1:, 1:3])