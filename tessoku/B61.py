import pprint

n, m = map(int, input().split())
a, b = [], []

for _ in range(m):
    ai, bi = map(int, input().split())
    a.append(ai)
    b.append(bi)

g = [[] for _ in range(n + 1)]

for i in range(m):
    g[a[i]].append(b[i])
    g[b[i]].append(a[i])

ans = 0
for i in range(1, n + 1):
    if len(g[ans]) < len(g[i]):
        ans = i

print(ans)
