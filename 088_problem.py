import numpy as np

data = np.array([
    [101, 85],
    [102, 65],
    [103, 95],
    [104, 75]
])

sorted_data = data[data[:, 1].argsort()]

print("Sorted by marks:")
print(sorted_data)