#!/usr/bin/env python3

from_file = __import__('2-from_file').from_file
rename = __import__('3-rename').rename

df = from_file('coinbase.csv', ',')

df = rename(df)

print(df.tail())