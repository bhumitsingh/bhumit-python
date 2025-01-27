"""
NumPy:
    NumPy is a powerful library for numerical computing in Python.

Overview of NumPy:
    - Numerical Cumputing: NumPy is primarily used for performing numerical calculations and operations efficiently.
    - N-Dimensional Arrays: It introduces a poerful N-Dimensional array object called ndarray, which allows for fast and flexible
                            operations on large datasets.
    - Mathematical Functions: Provides wide range of mathematical functions for performing operations on arrays, such as trigonometric,
                              statistical, and algebratic funcitons.

Key Features of NumPy:
    - Performance: NumPy is optimised for performance, allowing for operations to be executed in compiled C code, which is faster than
                   native pyhton code.
    - Broadcasting: This feature allows arithmetic operations to be performed on an array of different shapes and sizes.
    - Integeration: It integrates well with other libraries, such as SciPy, Pandas and Matplotlib, making it a cornerstone of
                    scientific Python ecosystem.

Common Use Cases of NumPy:
    Data Analysis: NumPy arrays are often used in data analysis and manipulation tasks.
    Machine Learning: It's widely used in machine learning algorithms for handling data and computation.
    Image-Processing: NumPy arrays can represent images, allowing for pixel-based operations.

"""

import numpy as np

# Creating a NumPy array
array = np.array([1,2,3,4,5,6])

# Performing a mathematical operation
squared_array = array**2

print(squared_array)