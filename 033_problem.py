import numpy as np

arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

result = np.ravel(arr)

print("Original:")
print(arr)

print("\nRavel:")
print(result)