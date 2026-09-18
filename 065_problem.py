import numpy as np

arr = np.array([5, 15, 25, 35, 45])

print("Original:", arr)
print("Clipped:", np.clip(arr, 10, 30))