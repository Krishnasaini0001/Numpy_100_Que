import numpy as np

marks = np.array([35, 72, 28, 90, 45, 63, 19, 81])

pass_marks = 40

passed = marks >= pass_marks
failed = marks < pass_marks

print("Marks:", marks)
print("Passed Students:", np.count_nonzero(passed))
print("Failed Students:", np.count_nonzero(failed))
print("Passed Marks:", marks[passed])
print("Failed Marks:", marks[failed])