import numpy as np

# 1D Array
arr = np.array([10, 20, 30, 40])
print(arr)

new_arr = np.delete(arr, 2)
print(new_arr)

# 2D Array
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2)

new_arr2 = np.delete(arr2, 0, axis=0)
print(new_arr2)
