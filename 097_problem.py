import numpy as np

data = np.array([10, 20, 30, 40, 50])

minimum = np.min(data)
maximum = np.max(data)

normalized = (data - minimum) / (maximum - minimum)

print("Original Data:", data)
print("Normalized Data:", normalized)