import numpy as np

arr1 = np.array([1, 2, np.nan, 4, 5])

new_arr1 = np.nan_to_num(arr1)
print(new_arr1)
