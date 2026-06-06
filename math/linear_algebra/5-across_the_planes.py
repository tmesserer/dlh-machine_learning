#!/usr/bin/env python3
"""Module for linear algebra"""


def matrix_shape(matrix):
    """checks the shape of a matrix, but
    more as a first-explorer. Does not
    work for non-rectangular, e.g."""
    shape = []
    while isinstance(matrix, list):
        if not matrix:
            return None
        shape.append(len(matrix))
        matrix = matrix[0]
    return shape


def add_matrices2D(mat1, mat2):
    """checks if matrices are same shape.
    If they are, returns an element-wise addition."""
    if matrix_shape(mat1) != matrix_shape(mat2):
        return None
    new_matrix = []
    new_row = []
    for i in range(0, len(mat1)):
        # print(f"i = {i}")
        for j in range(0, len(mat1[i])):
            # print(f"j = {j}")
            new_row.append(mat1[i][j] + mat2[i][j])
            # print(f"new row: {new_row}")
        new_matrix.append(new_row)
        new_row = []
    return new_matrix
