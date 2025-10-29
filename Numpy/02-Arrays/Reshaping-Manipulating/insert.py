import numpy as np

# insertion in 1D Array
arr1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(arr1)

new_arr_1D = np.insert(arr1, 2, 100)
print(new_arr_1D)

# insertion in 2D Array
arr2 = np.array([[1, 2], [3, 4]])
print(arr2)

# new_arr_2D = np.insert(arr2, 1, [5, 6], 0)
# new_arr_2D = np.insert(arr2, 1, [5, 6], 1)
new_arr_2D = np.insert(arr2, 1, [5, 6], None)
print(new_arr_2D)
