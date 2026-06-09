#!/usr/bin/env python3
"""Module for linear algebra"""


def np_elementwise(mat1, mat2):
    """Returns the shape of a NumPy array."""
    return (mat1 + mat2, mat1 - mat2, mat1 * mat2, mat1 / mat2)


"""
mat1 = np.array([[11, 22, 33], [44, 55, 66]])
mat2 = np.array([[1, 2, 3], [4, 5, 6]])
np_elementwise(mat1, mat2)
print(mat1 + mat2, mat1 - mat2, mat1 * mat2, mat1 / mat2)
print(mat1)
print(mat2)
"""
