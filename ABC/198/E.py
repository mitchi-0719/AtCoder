import sys

sys.setrecursionlimit(10**9)

n = int(input())
c = [None] + list(map(int, input().split()))
g = [[] for _ in range(n + 1)]
col_count = [0 for _ in range(10**5 + 10)]
ans = []

for i in range(n - 1):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)


def dfs(parent, pos):
    if col_count[c[pos]] == 0:
        ans.append(pos)

    col_count[c[pos]] += 1
    for i in g[pos]:
        if i != parent:
            dfs(pos, i)
    col_count[c[pos]] -= 1


dfs(None, 1)
for i in sorted(ans):
    print(i)
