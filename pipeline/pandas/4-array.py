#!/usr/bin/env python3
"""Module for using the pandas module in Python"""


def array(df):
    """function that takes a pd.DataFrame as input and modifies it"""
    new_array = df[["High", "Close"]].tail(n=10).to_numpy()
    return new_array
