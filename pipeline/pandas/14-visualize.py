#!/usr/bin/env python3
"""Module for using the pandas module in Python"""
import matplotlib.pyplot as plt
import pandas as pd
from_file = __import__('2-from_file').from_file

df = from_file('coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv', ',')
# df = from_file('coinbase.csv', ',')

df.drop("Weighted_Price", axis=1, inplace=True)

df.rename(columns={"Timestamp": "Date"}, inplace=True)
df["Date"] = pd.to_datetime(df["Date"], unit="s")
df.index = df["Date"]
df = df.drop("Date", axis=1)


df[["Close"]] = df[["Close"]].ffill(axis=0)

# fill with content of "Close"
cols_to_fill = ["High", "Low", "Open"]
for col in cols_to_fill:
    df[col] = df[col].fillna(df["Close"])

# Set missing values in Volume_(BTC) and Volume_(Currency) to 0
df[["Volume_(BTC)", "Volume_(Currency)"]] = \
    df[["Volume_(BTC)", "Volume_(Currency)"]].fillna(0,
                                                     axis=0)

df_plot = df.loc["2017":]
df_plot = df_plot.resample("D").agg({
    "High": "max",
    "Low": "min",
    "Open": "mean",
    "Close": "mean",
    "Volume_(BTC)": "sum",
    "Volume_(Currency)": "sum",
})

print(df_plot)
df_plot.plot()

# %%
