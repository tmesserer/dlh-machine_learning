#!/usr/bin/env python3
"""Module for linear algebra"""


def matrix_shape(matrix):
    """returns the shape of a matrix.
    args: matrix
    """
    this_row = matrix
    shape = []

    while isinstance(this_row, list):
        if not this_row:
            return [0]
            break
        shape.append(len(this_row))
        this_row = this_row[0]
    return shape
