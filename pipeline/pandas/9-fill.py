#!/usr/bin/env python3
"""Module for using the pandas module in Python"""


def fill(df):
    """function that takes a pd.DataFrame as input and modifies it"""
    df.drop("Weighted_Price", axis=1, inplace=True)  # remove column
    # fill with previous row:
    df[["Close"]] = df[["Close"]].ffill(axis=0)

    # fill with content of "Close"
    cols_to_fill = ["High", "Low", "Open"]
    for col in cols_to_fill:
        df[col] = df[col].fillna(df["Close"])

    # Sets missing values in Volume_(BTC) and Volume_(Currency) to 0
    df[["Volume_(BTC)", "Volume_(Currency)"]] = \
        df[["Volume_(BTC)", "Volume_(Currency)"]].fillna(0,
                                                         axis=0)
    return df


# new_frame = pd.read_csv("bitstamp.csv", sep=",")
# print(new_frame.head)
