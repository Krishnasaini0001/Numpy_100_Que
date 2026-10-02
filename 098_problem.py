import numpy as np

data = np.array([10, 12, 15, 18, 20, 22, 25])

mean = np.mean(data)
std = np.std(data)

z_scores = (data - mean) / std

print("Data:", data)
print("Mean:", mean)
print("Standard Deviation:", std)
print("Z-Scores:", z_scores)