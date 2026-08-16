#!/usr/bin/env python3

from_file = __import__('2-from_file').from_file
high = __import__('7-high').high

df = from_file('coinbase.csv', ',')

df = high(df)

print(df.head())