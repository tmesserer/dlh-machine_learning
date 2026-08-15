#!/usr/bin/env python3
"""Module for using the pandas module in Python"""
import pandas as pd


def from_file(filename, delimiter):
    """function that loads data from a file as a pd.DataFrame"""
    new_frame = pd.read_csv(filename, sep=delimiter)
    return new_frame
