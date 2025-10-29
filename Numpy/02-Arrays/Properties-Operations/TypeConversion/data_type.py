# changing the type of the array

import numpy as np

arr = np.array([1, 2, 3])
print(arr.dtype)

float_arr = arr.astype(np.float32)
print(float_arr.dtype)
