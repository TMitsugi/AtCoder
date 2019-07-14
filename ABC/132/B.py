# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 21:54:26 2019

@author: tomonori
"""

n=int(input())
p=list(map(int,input().split()))
count=0
for i in range(1,n-1):
    if p[i]>p[i-1]:
        if p[i+1]>p[i]:
            count=count+1
    elif p[i]>p[i+1]:
        if p[i-1]>p[i]:
            count+=1
print(count)