import numpy as np

arr = np.array([10, 20, 30])

result = np.expand_dims(arr, axis=0)

print("Original shape:", arr.shape)
print("New shape:", result.shape)
print(result)