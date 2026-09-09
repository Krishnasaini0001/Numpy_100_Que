import numpy as np

arr = np.arange(1, 10).reshape(3, 3)

lower = np.tril(arr)

print("Original Matrix:")
print(arr)

print("\nLower Triangular Matrix:")
print(lower)