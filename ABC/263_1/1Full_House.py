#正解

alfa = list(map(int, input().split()))
cntList = [0] * 5

for i in range(5):
    for j in range(5):
        if alfa[i] == alfa[j]:
            cntList[i] += 1

cnt2 = 0
cnt3 = 0
for i in range(5):
    if cntList[i] == 3:
        cnt3 += 1
    if cntList[i] == 2:
        cnt2 += 1
if cnt3 == 3 and cnt2 == 2:
    print("Yes")
else:
    print("No")