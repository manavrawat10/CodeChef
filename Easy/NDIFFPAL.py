# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 11:48:21 2018

@author: Manav
"""

#t=int(input())
#for i in range(t):
#    str='abc'
#    n=int(input())
#    output=''
#    k=0
#    for j in range(n):
#       output+=str[k%3]
#       k=k+1
#    print(output)

t = int(input())

while t>0:
	n = int(input())
	s = ''
	for i in range(n):
		ii = i
		if(i>=26):
			ii=ii%26

		num = 97+ii
		s = s+chr(num)

	print(s)

	t-=1