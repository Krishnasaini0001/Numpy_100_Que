import numpy as np

salaries = np.array([
    25000, 32000, 45000,
    38000, 52000, 60000,
    41000, 75000
])

print("Salaries:", salaries)

print("Average Salary:", np.mean(salaries))
print("Highest Salary:", np.max(salaries))
print("Lowest Salary:", np.min(salaries))

high_salary = salaries[salaries > 50000]

print("Employees earning above 50000:", high_salary)