import numpy as np

arr = np.array([10, 20, 30, 40, 50])

result = np.where(arr >= 30, "Pass", "Fail")

print("Result:", result)