import numpy as np

np.random.seed(42)

matrix = np.random.randint(1, 101, size=(5, 5))

print("Random Matrix:")
print(matrix)

print("\nMaximum:", np.max(matrix))
print("Minimum:", np.min(matrix))
print("Mean:", np.mean(matrix))
print("Standard Deviation:", np.std(matrix))
print("Sum:", np.sum(matrix))