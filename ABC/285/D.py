from collections import defaultdict
import sys

sys.setrecursionlimit(10**8)


def dfs(g, s, visited, finished):
    visited[s] = True
    for nex in g[s]:
        if not visited[nex]:
            dfs(g, nex, visited, finished)
        elif not finished[nex]:
            print("No")
            exit()
    finished[s] = True


n = int(input())
g = defaultdict(list)
names = set()
visited = defaultdict(bool)
finished = defaultdict(bool)

for _ in range(n):
    si, ti = input().split()
    g[si].append(ti)
    visited[si] = False
    finished[si] = False
    names.add(si)

for s in names:
    if not visited[s]:
        dfs(g, s, visited, finished)

print("Yes")
