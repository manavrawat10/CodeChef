# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 15:46:56 2018

@author: Manav
"""
import sys
T=int(input())
if 1<=T<=1000:
    lt=[]
    for c in range(T):
        inp=input()
        temp=inp.split(" ")
        temp=list(map(int, temp))
        temp.sort()
        lt.append(temp)
    #print(lt)
    for temp in lt:
        if len(temp)==4:
            for x in temp:
                if x>10000:
                    sys.exit
        else:
            sys.exit
    for x in lt:
        if x[0]==x[1] and x[2]==x[3]:
            print("YES")
        else:
            print("NO")