S=input()
flag_count=len(S)
Counter=0
for i in range(len(S)):
    for j in range(len(S)):
        if S[i]==S[j]:
            Counter+=1
    if Counter==2:
        flag_count=flag_count-1
    Counter=0
if flag_count == 0:
    print("Yes")
else:
    print("No")