# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 22:51:18 2019

@author: tomonori
"""
#少しいろいろ挑戦してみた
import sys
L,R=map(int,input().split())
modifyed=[]
flag=0
for i in range(L,R+1):
    modifyed.append(i%2019)
    if i%2019==0:
        print(0)
        sys.exit()
ans=[]
for m in range(len(modifyed)):
    for j in range(m+1,len(modifyed)):
        ans.append(modifyed[m]*modifyed[j]%2019)
        if modifyed[m]*modifyed[j]%2019==0:
          print(0)
          sys.exit()
print(min(ans))
