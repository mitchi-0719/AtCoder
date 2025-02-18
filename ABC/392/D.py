from collections import defaultdict

n = int(input())
k = []
a = []
count = []

for _ in range(n):
    i = list(map(int, input().split()))
    k.append(i[0])
    a.append(i[1:])
    d = defaultdict(int)
    for ai in i[1:]:
        d[ai] += 1
    count.append(d)

ans = 0

for i in range(n):
    for j in range(n):
        if i == j:
            continue

        cnt = 0
        si = set(count[i].keys())
        sj = set(count[j].keys())
        for v in si & sj:
            cnt += count[i][v] * count[j][v]

        ans = max(ans, cnt / (k[i] * k[j]))

print(ans)
