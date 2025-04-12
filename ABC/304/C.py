import sys

sys.setrecursionlimit(10**8)

n, d = map(int, input().split())
xy = [list(map(int, input().split())) for _ in range(n)]
contacts = [[] for _ in range(n)]
visited = [False] * n


def yes_no(b):
    return "Yes" if b else "No"


def is_inside(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) <= d**2


def dfs(g, i, visited):
    if visited[i]:
        return

    visited[i] = True
    for v in g[i]:
        dfs(g, v, visited)


for i in range(n - 1):
    for j in range(i + 1, n):
        if i == j:
            continue

        if is_inside(*xy[i], *xy[j]):
            contacts[i].append(j)
            contacts[j].append(i)

dfs(contacts, 0, visited)

for i in range(n):
    print(yes_no(visited[i]))
