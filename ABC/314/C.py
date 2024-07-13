from collections import defaultdict

n, m = map(int, input().split())
s = list(input())
c = list(map(int, input().split()))
d = defaultdict(list)

for i in range(n):
    d[c[i]].append(s[i])

idx = [-1 for _ in range(m)]
for ci in c:
    print(d[ci][idx[ci - 1] % len(d[ci])], end="")
    idx[ci - 1] += 1

print()
