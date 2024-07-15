import sys

sys.setrecursionlimit(10**6)


def solve(g, before, v, visited):
    if len(g[v]) == 1 and g[v][0] == before:
        return True

    if visited[v]:
        return False

    visited[v] = True
    ans = False
    for nex in g[v]:
        if nex == before:
            continue
        ans = ans or solve(g, v, nex, visited)

    return ans


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
ans = False

for v in g[0]:
    visited[0] = True
    for vi in g[v]:
        ans = ans or solve(g, v, vi, visited)

visited_set = set(visited)
print(visited_set, visited)
print("Yes" if ans and len(visited_set) == 1 and list(visited_set)[0] else "No")
