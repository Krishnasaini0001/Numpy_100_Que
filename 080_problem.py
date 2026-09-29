import numpy as np

arr = np.array([10, 25, 40, 55, 70, 85])

mask = (arr > 30) & (arr < 80)

result = arr[mask]

print("Filtered values:", result)