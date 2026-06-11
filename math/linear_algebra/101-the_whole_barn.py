#!/usr/bin/env python3
"""Module for linear algebra"""


def add_matrices(mat1, mat2):
    """adds two matrices.
    arguments:
        matrix
        axes: as a dictionary, where the value is a tuple"""

    if isinstance(mat1, list) and isinstance(mat2, list):
        if len(mat1) != len(mat2):
            return None
        else:
            return [add_matrices(mat1, mat2) for mat1, mat2 in zip(mat1, mat2)]
    elif isinstance(mat1, list) or isinstance(mat2, list):
        return None
    else:
        return (mat1 + mat2)
