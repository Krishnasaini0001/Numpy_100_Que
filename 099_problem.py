import numpy as np

study_hours = np.array([1, 2, 3, 4, 5, 6])
marks = np.array([45, 50, 58, 65, 75, 85])

correlation_matrix = np.corrcoef(study_hours, marks)

print("Study Hours:", study_hours)
print("Marks:", marks)

print("\nCorrelation Matrix:")
print(correlation_matrix)

print("\nCorrelation:", correlation_matrix[0, 1])