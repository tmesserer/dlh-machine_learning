#!/usr/bin/env python3
"""Module for linear algebra"""
import numpy as np


def np_slice(matrix, axes={}):
    """a matrix alongside a defined axis.
    arguments:
        matrix
        axes: as a dictionary, where the value is a tuple"""
    idx = []
    idx = [slice(None)] * matrix.ndim

    for axis, value in axes.items():
        idx[axis] = slice(*value)
    sliced_matrix = matrix[tuple(idx)]
    return sliced_matrix
