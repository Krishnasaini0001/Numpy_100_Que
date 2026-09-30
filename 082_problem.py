import numpy as np

matrix = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print("Sum of all elements:", np.sum(matrix))
print("Column-wise sum:", np.sum(matrix, axis=0))
print("Row-wise sum:", np.sum(matrix, axis=1))