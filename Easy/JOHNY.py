# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 14:56:50 2018

@author: 599798
"""
for _ in range(int(input())):
    input()
    lt=list(map(int,input().split()))
    pos=int(input())
    num=lt[pos-1]
    lt.sort()
    print(lt.index(num)+1)