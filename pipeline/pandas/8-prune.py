#!/usr/bin/env python3
"""Module for using the pandas module in Python"""


def prune(df):
    """function that takes a pd.DataFrame as input and modifies it"""
    df.dropna(axis=0, subset="Close", inplace=True)
    return df


# new_frame = pd.read_csv("bitstamp.csv", sep=",")
# print(new_frame.head)
