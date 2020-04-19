# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 18:41:08 2018

@author: 599798
"""

for _ in range(int(input())):
    n,lt=int(input()), list(map(int,input().split()))
    lt.sort()
    i=1
    while(i<n):
        if (lt[i]-lt[i-1]) not in [1,-1,0]:
            print("NO")
            break
        i+=1
    else:
        print("YES")
            
            