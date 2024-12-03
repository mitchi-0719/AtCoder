from collections import defaultdict


def dfs(start, s, visited):
    nexts = d[s]

    if start == s:
        print("No")
        exit()

    if visited[s]:
        return

    visited[s] = True

    for nex in nexts:
        dfs(start, nex, visited)

    visited[s] = False


n = int(input())
d = defaultdict(list)
visited = defaultdict(bool)
for _ in range(n):
    si, ti = input().split()
    d[si].append(ti)
    visited[si] = False

for start in d.keys():
    dfs(start, start, visited)

print("Yes")
