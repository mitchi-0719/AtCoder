k = int(input())

ans = []
num = "9876543210"

for i in range(2**10):
    cnt = 0
    tmp = []
    for j in range(10):
        if i & (1 << j):
            tmp += [num[j]]
    if len(tmp) != 0:
        ans.append(int(("".join(tmp))))

print(sorted(ans)[k])
