# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 13:30:56 2018

@author: Manav
"""
import math
for _ in range(int(input())):
    n,s=map(int,input().split())
    # for max volumn we have to make 2 sides of same length
    # volumn = a*a*c
    # 4*a + 4*a + 4*c = n
    # 2*a + c = n/4
    # c = n/4 -2*a
    
    # area of cuboid
    # 2*(a*a + a*c + a*c) = s
    # (a*a + 2*a*c) = s/2
    # a*a + 2*a*(n/4 -2*a) = s/2
    # a*a + a*n/2 - 4*a*a = s/2
    # a*n/2 = s/2 + 3*a*a
    # 3*a*a - n/2*a + s/2 = 0
    # 6*a*a -n*a + s = 0
    
    # solving quadratic equation
    # a = (-b + sqrt(b*b-4*a1*c))/2*a1
    # a = (-b - sqrt(b*b-4*a1*c))/2*a1
    a1=(n + math.sqrt(n*n - 24*s))/12
    a2=(n - math.sqrt(n*n - 24*s))/12
    c1 = n/4-2*a1
    c2 = n/4-2*a2
    if a1*a1*c1 > a2*a2*c2:
        print(a1*a1*c1)
    else:
        print(a2*a2*c2)
        
    
    