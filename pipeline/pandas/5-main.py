#!/usr/bin/env python3

from_file = __import__('2-from_file').from_file
slice = __import__('5-slice').slice

df = from_file('coinbase.csv', ',')

df = slice(df)

print(df.tail())