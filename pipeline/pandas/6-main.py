#!/usr/bin/env python3

from_file = __import__('2-from_file').from_file
flip_switch = __import__('6-flip_switch').flip_switch

df = from_file('coinbase.csv', ',')

df = flip_switch(df)

print(df.tail(8))