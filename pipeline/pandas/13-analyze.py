#!/usr/bin/env python3
"""Module for using the pandas module in Python"""
import pandas as pd
index = __import__('10-index').index


def analyze(df):
    """function that takes a pd.DataFrame as input and describes the data"""
    df.drop("Timestamp", axis=1, inplace=True)
    return df.describe(include='all')


# concat(df1, df2)
# df1 = pd.read_csv('coinbase.csv', sep=',')
# df2 = pd.read_csv('bitstamp.csv', sep=',')

# new_frame = pd.read_csv("bitstamp.csv", sep=",")
# print(new_frame.head)
