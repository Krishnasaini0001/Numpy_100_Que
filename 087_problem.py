import numpy as np

matrix = np.array([
    [1, 2],
    [3, 4],
    [1, 2],
    [5, 6]
])

result = np.unique(matrix, axis=0)

print("Unique rows:")
print(result)