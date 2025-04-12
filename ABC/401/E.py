n, m = map(int, input().split())
g = [[] for _ in range(n + 1)]


for _ in range(m):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)
