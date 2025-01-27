"""
The NumPy's main object is the homogeneous multidimensional array. It is a table (usually numbers), all the same type, indexed by a tuple of
non-negative integers. In NumPy, dimensions are called axes.
NumPy's array class is called ndarray. It is also known by the alias array.
"""

# Attributes of ndarray object

import numpy as np

array = np.array([[0,1,2,3,4],
                  [5,6,7,8,9],
                  [10,11,12,13,14]])

print(array.shape) # print the shape of the array

print(array.ndim) # print the number of dimensions of the array

print(array.dtype.name) # print the data type of the array

print(array.itemsize) # print the size of each element in the array

print(type(array)) # print the type of the array

# Array Creation

# Array creartion with regular Pyhton list or tuple
a = np.array([2, 3, 4])
print(a) # Output: [2 3 4]
print(a.dtype)
b = np.array([2.3, 4.3, 5.1])
print(b) # Output: [2.3 4.3 5.1]
print(b.dtype)

# Specifying type of array explicitly at cration time
c = np.array([2, 3, 4], dtype=complex)
print(c)

# Array creation with intial placeholders

a = np.zeros((3,4))
print(a)

b = np.ones((4,5))
print(b)

# Array Creation with arange function

a = np.arange(10, 30, 5)
print(a)

b = np.arange(0, 2, 0.3)
print(b)

# Using linespace for floating point
a = np.linspace(0, 2, 9)
print(a)
