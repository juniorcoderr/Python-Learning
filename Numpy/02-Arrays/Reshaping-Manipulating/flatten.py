# flattening array

import numpy as np

arr = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])

# affects original array
print(arr.ravel())

# does not affects original array
print(arr.flatten())
