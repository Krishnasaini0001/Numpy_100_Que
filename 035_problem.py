import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

result = np.concatenate((a, b))

print("Array A:", a)
print("Array B:", b)
print("Concatenated:", result)