import numpy as np
N,L=map(int,input().split())
Taste=list(int(i) for i in range(L+1-1,L+N-1+1) )
MaxTaste=[sum(Taste)]*N
print(sum(Taste)-Taste[np.argmin(np.abs(np.array(Taste)))])