c1 = list(map(int, input().split()))
c2 = list(map(int, input().split()))


cnt = 0
for i in range(3):
    if (
        c1[i] < c2[i] < c1[i + 3]
        or c1[i] < c2[i + 3] < c1[i + 3]
        or (c1[i] <= c2[i] <= c1[i + 3] and c1[i] <= c2[i + 3] <= c1[i + 3])
        or (c2[i] <= c1[i] <= c2[i + 3] and c2[i] <= c1[i + 3] <= c2[i + 3])
    ):
        cnt += 1

if cnt == 3:
    print("Yes")
else:
    print("No")
