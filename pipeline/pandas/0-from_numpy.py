#!/usr/bin/env python3
"""Module for using the pandas module in Python"""
import pandas as pd


def from_numpy(array):
    """function that creates a pd.DataFrame from a np.ndarray"""
    new_frame = pd.DataFrame(array, columns=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
                             [0:len(array[0])])
    return new_frame
