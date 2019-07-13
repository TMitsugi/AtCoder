# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 22:14:10 2019

@author: tomonori
"""
import numpy as np
N,D=map(int,input().split())
X=[]
dist=[]
Xsumnow=0
Xsumnext=0

for i in range(N):
    X.append([int(j) for j in input().split()])
count=N
for m in range(N):
    for j in range(m+1,N):
        for k in range(D):
            Xsumnow+=abs(X[j][k]-X[m][k])*abs(X[j][k]-X[m][k])
        dist.append(np.sqrt(Xsumnow))
        Xsumnow=0
TrueCounter=0
for l in range(len(dist)):
    if dist[l].is_integer():
        TrueCounter+=1

print(TrueCounter)