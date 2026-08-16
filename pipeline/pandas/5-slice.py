#!/usr/bin/env python3
"""Module for using the pandas module in Python"""
import pandas as pd


def slice(df):
    """function that takes a pd.DataFrame as input and modifies it"""
    new_frame = df.loc[::60, ["High", "Low", "Close", "Volume_(BTC)"]]
    return new_frame


# new_frame = pd.read_csv("bitstamp.csv", sep=",")
# print(new_frame.head)
