# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 16:45:19 2018

@author: 599798
"""
def convert(num,base):
    st=[]
    while num>1:
        #print(num%base)
        st.append(num%base)
        num//=base
        
    st.append(num)
    st.reverse()
    return st

a,n,s=map(int,input().split())
lt=convert(a,n+1)
for _ in range(abs(s-len(lt))):
    lt.append(0)
print(lt)
print(*lt[:s])