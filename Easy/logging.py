# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 15:32:39 2018

@author: 599798
"""
from itertools import combinations
for no in range(int(input())):
    n,m=map(int,input().split())
    lt=[]
    for _ in range(n):
        lt.append(int(input()))
    for i in range(1,n+1):
        comb=combinations(lt,i)
        csum=[sum(e) for e in comb]
        if m in csum:
            print("YES")
            break
    else:
        print("NO")