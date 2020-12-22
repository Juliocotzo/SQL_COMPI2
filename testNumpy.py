import numpy as np

arr1 = np.array([[1, 2], [3, 4]])

arr2 = np.array([[5, 6,7], [7, 8,10]])

arr = np.concatenate((arr1, arr2), axis=1)

print(arr[0][2])

print([1,2,3,5])
