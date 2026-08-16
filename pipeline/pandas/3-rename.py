#!/usr/bin/env python3
"""Module for using the pandas module in Python"""
import pandas as pd


def rename(df):
    """function that takes a pd.DataFrame as input and modifies it"""
    df.rename(columns={"Timestamp": "Datetime"}, inplace=True)
    df["Datetime"] = pd.to_datetime(df["Datetime"], unit='s')
    return df[["Datetime", "Close"]]

# Checking the file and format:
# new_frame = pd.read_csv("bitstamp.csv", sep=",")
# print(new_frame.head)
