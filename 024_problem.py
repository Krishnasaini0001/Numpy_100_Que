import numpy as np

arr = np.arange(1, 10).reshape(3, 3)

upper = np.triu(arr)

print("Original Matrix:")
print(arr)

print("\nUpper Triangular Matrix:")
print(upper)