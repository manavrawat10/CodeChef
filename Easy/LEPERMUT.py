# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 09:49:39 2018

@author: Manav
"""

t=int(input())
final=[]
for i in range(t):
    n=int(input())
    ele=list(map(int,input().split()))
    lo,to=0,0
    for j in range(len(ele)-1):
        if ele[j]>ele[j+1]:
            lo+=1
        for k in range(j+1,len(ele)):
            if ele[j]>ele[k]:
                to+=1
    if to==lo:
        final.append("YES")
    else:
        final.append("NO")
print(*final, sep="\n")