N=int(input())
a=[0]*(N)
maxim=[0]*(N)
for i in range(N):
    a[i]=int(input())
maxim=sorted(list(a), reverse=True)
for k in range(N):
    if a[k]!=maxim[0]:
        print(maxim[0])
    else:
        print(maxim[1])