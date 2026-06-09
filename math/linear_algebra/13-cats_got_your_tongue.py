#!/usr/bin/env python3
"""Module for linear algebra"""
import numpy as np


def np_cat(mat1, mat2, axis=0):
    """concatenates two matrices alongside an axis"""
    return np.concatenate((mat1, mat2), axis)
