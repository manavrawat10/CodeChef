# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 18:35:37 2018

@author: Manav
"""

for _ in range(int(input())):
    hr,mn=map(int, input().split())
    ct=0
    for h in range(hr):
        for m in range(mn):
            st=str(h)+str(m)
            if len(set(list(st))) == 1:
                ct+=1
    print(ct)
            