import sys

sys.setrecursionlimit(10**6)


def solve(g, dir_g, par, cur, child):
    if len(child) == 1 and child[0] == par:
        return

    for c in child:
        if c != par:
            dir_g[cur].append(c)
            solve(g, dir_g, cur, c, g[c])


def dfs(ans, dir_g, cur, child):
    if len(child) == 0:
        return -1
    m = 0
    for c in child:
        ans[c] = dfs(ans, dir_g, c, dir_g[c]) + 1
        m = max(m, ans[c])

    return m


n, t = map(int, input().split())
t -= 1
g = [[] for _ in range(n)]
dir_g = [[] for _ in range(n)]

for i in range(1, n):
    a, b = map(int, input().split())
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)

solve(g, dir_g, None, t, g[t])

ans = [0] * n
ans[t] = dfs(ans, dir_g, t, dir_g[t]) + 1

print(*ans)
