#!/usr/bin/env python3
"""Module for linear algebra"""


def add_arrays(arr1, arr2):
    """checks if arrays are same length.
    If they are, returns an element-wise addition."""
    if len(arr1) != len(arr2):
        return None
    sum_arr = []
    for i in range(0, len(arr1)):
        sum_arr.append(arr1[i] + arr2[i])
    return sum_arr
