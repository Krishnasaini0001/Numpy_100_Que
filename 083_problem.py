import numpy as np

matrix = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print("Column-wise mean:", np.mean(matrix, axis=0))
print("Row-wise mean:", np.mean(matrix, axis=1))