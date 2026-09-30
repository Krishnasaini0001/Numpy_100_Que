import numpy as np

marks = np.array([35, 55, 72, 88, 95])

result = np.where(
    marks >= 75,
    "Distinction",
    np.where(marks >= 40, "Pass", "Fail")
)

print("Marks:", marks)
print("Result:", result)