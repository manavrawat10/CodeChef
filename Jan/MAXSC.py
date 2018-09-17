# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 16:59:05 2018

@author: Manav
"""
import os
T=int(input())
if 1<=T<=10:
    summ=[]
    for c in range(T):
        N=int(input())
        if 1<=N<=700:
            lt=[]
            for i in range(N):
                A=input()
                temp=A.split(" ")
                temp=list(map(int, temp))
                temp.sort()
                lt.append(temp)
            print(lt)
            for x in lt:
                print(x)
                if (len(x)==N):
                    print("Yes")
                    for i in x:
                        if i<=0 or i>1000000000:
                            os._exit(0)
                else:
                    print("No")
                    os._exit(0)
            #print(lt)
            sum1=0
            for ele in lt:
                sum1=sum1+ele[N-1]
            if sum1<=3700:
                #print(sum1)
                summ.append(sum1)
    for s in summ:
        print(s)
        
        
        
        