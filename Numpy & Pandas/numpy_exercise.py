import numpy as np

# Program 1: Create two dimensional 3x3 array and perform ndim, shape, slicing
arr_2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("2D Array:")
print(arr_2d)
print("ndim:", arr_2d.ndim)
print("shape:", arr_2d.shape)
print("Slicing (first two rows):\n", arr_2d[:2])

# Program 2: Create one dimensional array and perform ndim, shape, reshape
arr_1d = np.array([1,2,3,4,5,6,7,8,9])
print("\n1D Array:")
print(arr_1d)
print("ndim:", arr_1d.ndim)
print("shape:", arr_1d.shape)
arr_reshaped = arr_1d.reshape((3,3))
print("Reshaped to 3x3:\n", arr_reshaped)