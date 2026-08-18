#!/usr/bin/env python3
"""Module for using the pandas module in Python"""


def index(df):
    """function that takes a pd.DataFrame as input and modifies it"""
    df.index = df["Timestamp"]
    df.drop("Timestamp", axis=1, inplace=True)
    return df


# new_frame = pd.read_csv("bitstamp.csv", sep=",")
# print(new_frame.head)
