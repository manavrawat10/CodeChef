# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 17:11:47 2018

@author: 599798
"""
def is_prime(num):
    if num%2==0:
        return False
    else:
        k=3
        while k<=(num/2+1):
            if num%k==0:
                return False
            k+=2
        return True
    
for _ in range(int(input())):
    a,b=map(int,input().split())
    k=1
    while True:
        if is_prime(a+b+k):
            print(k)
            break
        k+=1
