import numpy as np

# Create a one-dimensional array from 1 to 10
arr = np.arange(1, 11)

print("One-Dimensional NumPy Array:")
print(arr)

# Display array information
print("Number of dimensions:", arr.ndim)
print("Array shape:", arr.shape)
print("Data type:", arr.dtype)

# Access and slice array elements
print("First element:", arr[0])
print("Elements from index 2 to 5:", arr[2:6])

# Perform mathematical operations
print("Array + 5:", arr + 5)
print("Array multiplied by 2:", arr * 2)
print("Sum of elements:", np.sum(arr))
print("Mean of elements:", np.mean(arr))
