import numpy as np

arr = np.array([10, 20, 0, 40])

print("Any zero:", np.any(arr == 0))
print("Any value > 35:", np.any(arr > 35))