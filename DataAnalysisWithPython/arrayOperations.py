# Arithmetic operations on arrays apply elementwise
import numpy as np

a = np.array([10, 20, 30, 40, 50])
b = np.arange(5)
print(a)
print(b)

c = a + b # addition
print(c)
d = b - a # substraction
print(d)
r = b**2 # exponentiation
print(r)
sin = 10 * np.sin(a) # multiplication with a trigonometric function
print(sin)
print(a < 35) # comparison

# Matrix operations
A = np.array([[1, 1],
             [0, 1]])
B = np.array([[2, 0],
             [3, 4]])
C = A * B # element-wise multiplication
print(C)

D = A @ B # matrix multiplication
print(D) # Note: matrix multiplication is only available in numpy >= 1.10.0

E = A.dot(B) # matrix multiplication
print(E) # Note: matrix multiplication is only available in numpy >= 1.10.0


# Some operations, such as += and *=, act in place to modify an existing array rather than create a new one.

rg = np.random.default_rng(1) # random number generator

a = np.ones((2, 3), dtype = int)
b = rg.random((2, 3))

a *= 3
print(a)

b += a 
print(b)
"""
When operating with arrays of different types, the type of the resulting array corresponds to the more general or precise one 
(a behavior known as upcasting).
"""

from numpy import pi

a = np.ones(3, dtype=np.int32) # 32-bit integer array
b = np.linspace(0, pi, 3)

c = a + b # addition
print(c)

d = np.exp(c * 1j) # exponentiation with complex numbers
print(d)
print(d.dtype.name)

# Many unary operations, such as computing the sum of all the elements in the array, are implemented as methods of the ndarray class.

a = rg.random((2,3)) # random array

print(a)
print(a.sum()) # sum of all elements in the array

print(a.min()) # minimum value in the array

print(a.max()) # maximum value in the array

"""
By default, these operations apply to the array as though it were a list of numbers, regardless of its shape. However, by
specifying the axis parameter you can apply an operation along the specified axis of an array:
"""

b = np.arange(12).reshape(3,4)
print(b)

print(b.sum(axis=0)) # sum along the first axis (rows)
print(b.sum(axis=1)) # sum along the second axis (columns)

print(b.cumsum(axis=1)) # cumulative sum along the second axis (columns)





