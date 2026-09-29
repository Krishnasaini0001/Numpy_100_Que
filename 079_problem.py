import numpy as np

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

column = np.array([
    [10],
    [20]
])

result = matrix + column

print(result)