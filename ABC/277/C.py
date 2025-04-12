import sys
from collections import defaultdict

sys.setrecursionlimit(10**8)


def dfs(g, i, visited):
    if visited[i]:
        return

    visited[i] = True
    for v in g[i]:
        dfs(g, v, visited)


n = int(input())
g = defaultdict(list)

for _ in range(n):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1

    g[a].append(b)
    g[b].append(a)

visited = defaultdict(bool)
dfs(g, 0, visited)

ans = 0
for k, v in visited.items():
    ans = max(ans, k if v else 0)

print(ans + 1)
