#!/usr/bin/env python3
"""Module for linear algebra"""
import numpy as np


def np_shape(matrix):
    """Returns the shape of a NumPy array."""
    return matrix.shape


"""
def np_shape(matrix):
    gives the shape of a matrix.
    Args: matrix
    if isinstance(mat_shape, list):
        pass
    else:
        mat_shape = []
    mat_shape.append(len(matrix))
    if matrix.ndim > 1:
        return (len(matrix) + np_shape(matrix[0]))
"""
