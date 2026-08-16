#!/usr/bin/env python3
"""Module for using the pandas module in Python"""
import pandas as pd


def array(df):
    """function that takes a pd.DataFrame as input and modifies it"""
    new_array = np.array(df[["High", "Close"]].tail(n=10))
    return new_array


# Checking the file and format:
# new_frame = pd.read_csv("coinbase.csv", sep=",")
# print(new_frame.head)
