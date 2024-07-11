def dfs(g, dist, s, visited):
    visited[s] = True

    d = dist
    for v, c in g[s]:
        if visited[v]:
            continue

        d = max(d, dfs(g, dist + c, v, [*visited]))

    return d


n, m = map(int, input().split())
g = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    g[a].append((b, c))
    g[b].append((a, c))

ans = 0
for i in range(n + 1):
    ans = max(ans, dfs(g, 0, i, [False] * (n + 1)))

print(ans)
