#clear

l1, r1, l2, r2 = map(int, input().split())

if r1 < r2:
    li = [0]*r2
else:
    li = [0]*r1

for i in range(l1, r1):
    li[i] = 1

for i in range(l2, r2):
    li[i] += 1

cnt = 0
for i in li:
    if i == 2:
        cnt += 1

print(cnt)