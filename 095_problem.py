import numpy as np

temperature = np.array([
    32, 35, 34, 36, 38,
    37, 33, 31, 30, 35
])

print("Temperature:", temperature)

print("Average Temperature:", np.mean(temperature))
print("Maximum Temperature:", np.max(temperature))
print("Minimum Temperature:", np.min(temperature))

hot_days = temperature > 35

print("Hot Days:", np.count_nonzero(hot_days))
print("Temperatures above 35°C:", temperature[hot_days])