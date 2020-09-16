# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 19:12:21 2020

@author: chelr
"""

d = {}

with open('string_formatting.txt') as f:
    for line in f:
        (first, last) = line.split()
        d[first] = last
        print ("Good evening Dr. {lname}, would you mind if I called you {fname}?".format(lname = last, fname = first))
