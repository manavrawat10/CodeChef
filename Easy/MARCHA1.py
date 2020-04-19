# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 13:02:03 2018

@author: 599798
"""

""" Maximum sum from the array """


def calculate(arr):
    if len(arr)==1:
        return arr[0]
    elif len(arr)==0:
        return 0
    else:
        return arr[0]+max(calculate(arr[2:]), calculate(arr[3:]))
print(calculate([1,2,4,2,2,5]))