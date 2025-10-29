# extracting subset of data

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

print(arr[1:5])  # index 1 to 4
print(arr[:4])  # index 0 to 3
print(arr[::2])  # every second element
print(arr[::-1])  # return reverse array
