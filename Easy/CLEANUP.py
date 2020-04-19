# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 14:46:21 2018

@author: 599798
"""
"""
for _ in range(int(input())):
    total, done = list(map(int, input().split()))
    li = list(map(int, input().split()))
    this = []
    for i in range(1, total + 1):
        if i not in li:
            this.append(i)
    chef = []
    assiss = []
    for i in range(len(this)):
        if i % 2 != 0:
            assiss.append(this[i])
        else:
            chef.append(this[i])
    print(*chef)
    print(*assiss)
    """
print(int("12",2))