#!/usr/bin/env python3

from_file = __import__('2-from_file').from_file
array = __import__('4-array').array

df = from_file('coinbase.csv', ',')

A = array(df)

print(A)