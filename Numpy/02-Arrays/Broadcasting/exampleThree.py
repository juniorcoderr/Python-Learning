# error condition -> Incompatible shapes
import numpy as np

arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([4, 5])

result = arr1 + arr2
print(result)

# solution -> by using .reshape()
