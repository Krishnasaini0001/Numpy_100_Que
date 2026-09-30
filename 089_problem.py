import numpy as np

arr = np.array([45, 12, 89, 34, 67, 95, 23])

n = 3

top_values = np.sort(arr)[-n:][::-1]

print("Top", n, "values:", top_values)