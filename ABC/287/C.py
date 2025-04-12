import sys

sys.setrecursionlimit(10**6)


def yes_no(b):
    return "Yes" if b else "No"


def dfs(g, i, visited, parent):
    visited[i] = True
    for v in g[i]:
        if v == parent:
            continue
        if visited[v]:
            print("No")
            exit()

        dfs(g, v, visited, i)


n, m = map(int, input().split())
g = [[] for _ in range(n)]

for _ in range(m):
    u, v = map(int, input().split())
    u, v = u - 1, v - 1
    g[u].append(v)
    g[v].append(u)
    if len(g[u]) > 2 or len(g[v]) > 2:
        print("No")
        exit()

visited = [False] * n

dfs(g, 0, visited, None)
print(yes_no(visited.count(False) == 0))
