#!/usr/bin/env python3

from_file = __import__('2-from_file').from_file
concat = __import__('11-concat').concat

df1 = from_file('coinbase.csv', ',')
df2 = from_file('bitstamp.csv', ',')

df = concat(df1, df2)

print(df)