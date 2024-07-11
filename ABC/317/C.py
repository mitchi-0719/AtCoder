N, M = map(int, input().split())
E = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    E[a][b] = c
    E[b][a] = c

ans = 0
used = [False] * (N + 1)


def dfs(v, s):
    global ans
    used[v] = True
    if s > ans:
        ans = s
    for i in range(1, N + 1):
        if not used[i] and E[v][i]:
            dfs(i, s + E[v][i])
    used[v] = False


for i in range(1, N + 1):
    dfs(i, 0)

print(ans)
