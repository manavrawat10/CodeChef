# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 16:16:33 2018

@author: 599798
"""

""" Start and end position of element """


def binary_search(arr,k,l,r):

    while(l<=r):
        mid=(l+r)//2

        if arr[mid]==k:
            return mid,l,r
        elif arr[mid]>k:
            r=mid-1
        else:
            l=mid+1
    return -1
def find_last(arr,k):
    l=0
    r=len(arr)-1
    # call for the check of element present in the array
    value=binary_search(arr,k,l,r)
    
    if value!=-1:
        pos,l,r=value
        # check for the first most element
        value=binary_search(arr,k,l,pos-1)
        if value==-1:
            first=pos
        else:
            first=value[0]
        # check for the last most position of the element
        value=binary_search(arr,k,pos+1,r)
        if value==-1:
            last=pos
        else:
            last=value[0]
        
        print(first,last)
    else:
        print("Not found")
find_last([1,2,2,5,5,7,8,9,9,9,10,15,15,18,18,19],1)