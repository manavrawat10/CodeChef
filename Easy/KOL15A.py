# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 10:28:57 2018

@author: Manav
"""

for _ in range(int(input())):
    s=input()
    sum=0
    for i in s:
        if i.isdigit():
            sum+=int(i)
    print(sum)