#!/usr/bin/env python3
"""Module for using the pandas module in Python"""
import pandas as pd


df = pd.DataFrame(
    {
        "First": [0.0, 0.5, 1.0, 1.5],
        "Second": ["one", "two", "three", "four"]
    }, index=list("ABCD")
    )
