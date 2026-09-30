import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

result = np.stack((a, b))

print("Stacked array:")
print(result)

print("Shape:", result.shape)