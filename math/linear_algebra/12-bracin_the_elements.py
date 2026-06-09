#!/usr/bin/env python3
"""Module for linear algebra"""


def np_elementwise(mat1, mat2):
    """Returns the shape of a NumPy array."""
    return (mat1 + mat2, mat1 - mat2, mat1 * mat2, mat1 / mat2)
