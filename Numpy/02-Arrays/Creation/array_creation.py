# creating arrays from python lists
import numpy as np

arr1 = np.array([1, 2, 3, 4, 5, 6])
print(arr1)

# creating arrays with default values
# Array of zeros
arr2 = np.zeros(3)  # 1D array of zeros
print(arr2)

arr3 = np.zeros((3, 4))  # 3x4 array of zeros
print(arr3)

# Array of ones
arr4 = np.ones((2, 3))  # 2x3 array of ones
print(arr4)

# Array with a constant value
arr5 = np.full((2, 2), 7)  # 2x2 array filled with 7
print(arr5)

# Range of values
arr6 = np.arange(0, 10, 2)  # [0, 2, 4, 6, 8] (start, stop, step)
print(arr6)

# Identity matrix
arr7 = np.eye(3)  # 3x3 identity matrix
print(arr7)
