#!/usr/bin/env python3

from_file = __import__('2-from_file').from_file
prune = __import__('8-prune').prune

df = from_file('coinbase.csv', ',')

df = prune(df)

print(df.head())