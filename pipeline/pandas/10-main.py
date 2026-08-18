#!/usr/bin/env python3

from_file = __import__('2-from_file').from_file
index = __import__('10-index').index

df = from_file('coinbase.csv', ',')

df = index(df)

print(df.tail())