import numpy as np

arr = np.array([10, 45, 23, 89, 34])

index = np.argmin(arr)

print("Array:", arr)
print("Minimum index:", index)
print("Minimum value:", arr[index])