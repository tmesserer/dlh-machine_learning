#!/usr/bin/env python3
"""Module for linear algebra"""


def cat_arrays(arr1, arr2):
    """concatenates two arrays.
    Args:
        arr1: a list
        arr2: a list"""
    arr_new = []
    arr_new.extend(arr1)
    arr_new.extend(arr2)
    return arr_new
