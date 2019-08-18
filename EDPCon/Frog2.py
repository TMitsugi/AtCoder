import numpy as np
#numpyを使う理由は分かったがsysを使うところがまだ理解不足（おそらく計算時間）
n,k=map(int,input().split())
h=np.array(list(map(int,input().split())))
dp=np.zeros(n,dtype=int)
dp[1]=abs(h[1]-h[0])
for i in range(2,n):
    if i-k>0:
        dp[i]=min(dp[i-k:i]+abs(h[i]-h[i-k:i]))
    elif 0>=i-k:
        dp[i]=min(dp[0:i]+abs(h[i]-h[0:i]))
print(dp[n-1])