A,B=map(int,input().split())
PlusAB=A+B
KakeruAB=A*B
MinusAB=A-B
print(max(KakeruAB,max(PlusAB,MinusAB)))