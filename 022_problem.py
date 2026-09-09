import numpy as np

arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print("Array:")
print(arr)

print("\nDimensions:", arr.ndim)
print("Shape:", arr.shape)
print("Size:", arr.size)
print("Data type:", arr.dtype)
print("Item size:", arr.itemsize, "bytes")