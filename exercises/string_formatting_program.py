# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 19:12:21 2020

@author: chelr
"""

d = {}

with open('string_formatting.txt') as f:
    for line in f:
        (key, val) = line.split()
        d[key] = val
        print ("Good evening Dr.", val, ",", "would you ming if I called you",
                  key, "?")

