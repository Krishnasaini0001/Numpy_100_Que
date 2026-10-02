import numpy as np

np.random.seed(42)

data = np.random.randint(10, 101, 20)

print("Dataset:")
print(data)

print("\n--- Statistical Analysis ---")

print("Total:", np.sum(data))
print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Maximum:", np.max(data))
print("Minimum:", np.min(data))
print("Variance:", np.var(data))
print("Standard Deviation:", np.std(data))

print("\n--- Filtering ---")

above_average = data[data > np.mean(data)]

print("Values above average:", above_average)

print("\n--- Sorting ---")

print("Sorted Data:", np.sort(data))

print("\n--- Top 5 Values ---")

top_5 = np.sort(data)[-5:][::-1]

print("Top 5:", top_5)