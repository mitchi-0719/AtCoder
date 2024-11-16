n, m = map(int, input().split())

g = [[] for _ in range(n + 1)]
for i in range(m):
    u, v, w = map(int, input().split())
    g[u].append((v, w))

print(g)
