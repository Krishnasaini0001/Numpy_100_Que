import numpy as np

arr = np.array([10, 20, 30, 40, 50])

value = 30

positions = np.where(arr == value)

print("Array:", arr)
print("Search value:", value)
print("Position:", positions[0])