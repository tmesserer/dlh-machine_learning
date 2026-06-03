#!/usr/bin/env python3
"""Module for linear algebra"""
import numpy as np

def matrix_shape(matrix):
    """returns the shape of a matrix.
    args: matrix 
    """

mat1 = [[1, 2], [3, 4]]
print(matrix_shape(mat1))
mat2 = [[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]],
        [[16, 17, 18, 19, 20], [21, 22, 23, 24, 25], [26, 27, 28, 29, 30]]]

print(len(mat1))
array1 = np.ndarray(mat1)
print(array1.shape())