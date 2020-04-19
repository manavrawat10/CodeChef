# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 12:30:19 2018

@author: 599798
"""

a,b=map(int,input().split())
c=a-b
ch=c
while ch==c:
    last=c%10
    c=c//10
    last=(last-1)%10
    ch=c*10+last
print(ch)