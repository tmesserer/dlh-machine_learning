#!/usr/bin/env python3

from_file = __import__('2-from_file').from_file
analyze = __import__('13-analyze').analyze

df = from_file('coinbase.csv', ',')

stats = analyze(df)

print(stats)