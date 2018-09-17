# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 10:42:38 2018

@author: Manav
"""

t,b=input().split()
bi=list(b)
ai=list('abcdefghijklmnopqrstuvwxyz')
for _ in range(int(t)):
    s=input()
    ns=''
    for i in s:
        if i=='_':
            ns+=" "
        elif i in ['.',',','!','?']:
            ns+=i
        elif i.isupper():
            ns+=str(bi[ai.index(i.lower())]).upper()
        else:
            ns+=str(bi[ai.index(i)])
    print(ns)