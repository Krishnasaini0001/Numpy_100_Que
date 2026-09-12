import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60])

parts = np.split(arr, 3)

for i, part in enumerate(parts, start=1):
    print(f"Part {i}:", part)