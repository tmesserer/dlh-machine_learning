#!/usr/bin/env python3

from_file = __import__('2-from_file').from_file
hierarchy = __import__('12-hierarchy').hierarchy

df1 = from_file('coinbase.csv', ',')
df2 = from_file('bitstamp.csv', ',')

df = hierarchy(df1, df2)

print(df)