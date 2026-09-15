import numpy as np

arr = np.array([10, 45, 23, 89, 34])

index = np.argmax(arr)

print("Array:", arr)
print("Maximum index:", index)
print("Maximum value:", arr[index])