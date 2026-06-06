#!/usr/bin/env python3
"""Module for linear algebra"""


def matrix_transpose(matrix):
    """returns the transposed matrix of a matrix.
    args: matrix
    """
    new_matrix = []
    new_row = []
    # while isinstance(matrix[0], list):
    # matrix = matrix[0]
    if not matrix:
        return []
    for i in range(0, len(matrix[0])):
        for j in range(0, len(matrix)):
            new_row.append(matrix[j][i])
        new_matrix.append(new_row)
        new_row = []
    return new_matrix
