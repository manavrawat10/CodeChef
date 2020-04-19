# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 15:11:26 2018

@author: 599798
"""

for _ in range(int(input())):
    for _ in range(int(input())):
        a,b,c=map(int,input().split())
        if b%2==0:   # even number count will be equal
            print(int(b/2))
        else:
            # odd number opposite of a will be max as compared to other
            if a==c:
                print(int(b//2))
            else:
                print(int(b//2) +1)