# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 12:23:45 2018

@author: 599798
"""

for i in range(int(input())):
    x=int(input())
    counter=0
    d=5
    while d<=x:
        counter+=x//d
        d*=5
    print(counter)