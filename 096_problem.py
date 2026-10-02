import numpy as np

prices = np.array([
    499, 799, 1299, 999,
    1499, 699, 1999, 899
])

discount = 0.10

discounted_prices = prices - (prices * discount)

print("Original Prices:", prices)
print("Discounted Prices:", discounted_prices)
print("Average Original Price:", np.mean(prices))
print("Minimum Price:", np.min(prices))
print("Maximum Price:", np.max(prices))