import numpy as np

sales = np.array([
    25000, 32000, 28000, 41000,
    37000, 45000, 39000, 52000,
    48000, 55000, 61000, 58000
])

print("Monthly Sales:", sales)
print("Total Sales:", np.sum(sales))
print("Average Sales:", np.mean(sales))
print("Highest Sales:", np.max(sales))
print("Lowest Sales:", np.min(sales))