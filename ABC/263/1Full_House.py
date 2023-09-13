#正解

alfa = list(map(int, input().split()))
cntList = [0] * 5

for i in range(5):
    for j in range(5):
        if alfa[i] == alfa[j]:
            cntList[i] += 1

cnt = 0
for i in range(5):
    if cntList[i] == 3:
        cnt += 1
if cnt == 3:
    print("Yes")
else:
    print("No")