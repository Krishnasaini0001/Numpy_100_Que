import numpy as np

arr = np.array([10, 25, 40, 55, 70, 85])

filtered = arr[arr > 50]

print("Original array:", arr)
print("Values greater than 50:", filtered)