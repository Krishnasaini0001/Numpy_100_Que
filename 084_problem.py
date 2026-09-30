import numpy as np

arr = np.array([[[10, 20, 30]]])

print("Original shape:", arr.shape)

result = np.squeeze(arr)

print("New shape:", result.shape)
print("Result:", result)