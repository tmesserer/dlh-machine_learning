#!/usr/bin/env python3
"""Module for using the pandas module in Python"""


def high(df):
    """function that takes a pd.DataFrame as input and modifies it"""
    df.sort_values(by="High", ascending=False, inplace=True)
    return df


# new_frame = pd.read_csv("bitstamp.csv", sep=",")
# print(new_frame.head)
