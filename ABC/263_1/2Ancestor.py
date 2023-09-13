#answer

N=int(input())
P=[0,0]+list(map(int,input().split()))

crr=N  # いま注目している人
cnt=0  # いま注目している人が人Nの何代前か
while crr!=1:
    # 1代遡る
    cnt+=1
    crr=P[crr]

print(cnt)
