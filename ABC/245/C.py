import sys

sys.setrecursionlimit(10**6)


def dfs(g, n, dist, i, visited):
    visited[i] = True

    if dist == n - 1:
        print("Yes")
        exit()

    for v in g[i]:
        if visited[v]:
            continue
        dfs(g, n, dist + 1, v, visited)


n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
g = [[] for _ in range(2 * n)]

for i in range(n - 1):
    if abs(a[i] - a[i + 1]) <= k:
        g[i].append(i + 1)
    if abs(a[i] - b[i + 1]) <= k:
        g[i].append(i + 1 + n)
    if abs(b[i] - a[i + 1]) <= k:
        g[i + n].append(i + 1)
    if abs(b[i] - b[i + 1]) <= k:
        g[i + n].append(i + n + 1)

dfs(g, n, 0, 0, [False] * (2 * n))
dfs(g, n, 0, n, [False] * (2 * n))

print("No")
