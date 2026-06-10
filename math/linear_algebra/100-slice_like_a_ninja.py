#!/usr/bin/env python3
"""Module for linear algebra"""
import numpy as np


def np_slice(matrix, axes={}):
    """a matrix alongside a defined axis.
    arguments:
        matrix
        axes: as a dictionary, where the value is a tuple"""
    sliced_matrix = 
    return sliced_matrix

import numpy as np

mat1 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
# print(np_slice(mat1, axes={1: (1, 3)}))
print(mat1)
mat2 = np.array([[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]],
                 [[11, 12, 13, 14, 15], [16, 17, 18, 19, 20]],
                 [[21, 22, 23, 24, 25], [26, 27, 28, 29, 30]]])
# print(np_slice(mat2, axes={0: (2,), 2: (None, None, -2)}))
print(mat2)
slice = ()
print(slice(mat1))