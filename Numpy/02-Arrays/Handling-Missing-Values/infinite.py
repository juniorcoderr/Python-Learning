# handling infinite values
import numpy as np

arr1 = np.array([1, 2, np.inf, 4, 5])

print(np.isinf(arr1))
