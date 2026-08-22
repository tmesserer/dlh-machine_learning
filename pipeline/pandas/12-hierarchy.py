#!/usr/bin/env python3
"""Module for using the pandas module in Python"""
import pandas as pd
index = __import__('10-index').index


def hierarchy(df1, df2):
    """function that takes a pd.DataFrame as input and modifies it"""
    index(df1)
    index(df2)

    new_frame = pd.concat((df2.loc[1417411980:1417417980],
                           df1.loc[1417411980:1417417980]),
                          keys=["bitstamp", "coinbase"])
    new_frame = new_frame.swaplevel(0, 1)
    new_frame = new_frame.sort_index(ascending=[True, True])
    return new_frame


# concat(df1, df2)
# df1 = pd.read_csv('coinbase.csv', sep=',')
# df2 = pd.read_csv('bitstamp.csv', sep=',')

# new_frame = pd.read_csv("bitstamp.csv", sep=",")
# print(new_frame.head)
