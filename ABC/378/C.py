from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))
b = [-1 for _ in range(n)]
d = defaultdict(list)

for i in range(n):
    if len(d[a[i]]) >= 1:
        b[i] = d[a[i]][-1] + 1
    d[a[i]].append(i)

print(*b)
