import numpy as np

arr = np.array([0, 5, 0, 10, 15, 0])

positions = np.nonzero(arr)

print("Non-zero positions:", positions[0])