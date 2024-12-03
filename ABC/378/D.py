def isInRange(low, high, x):
    return low <= x < high


def dfs(i, j, level, visited):
    if not (
        isInRange(0, h, i)
        and isInRange(0, w, j)
        and not visited[i][j]
        and s[i][j] == "."
    ):
        return 0

    if level == k:
        return 1

    move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    cnt = 0
    visited[i][j] = True
    for dx, dy in move:
        nex_i = i + dy
        nex_j = j + dx
        cnt += dfs(nex_i, nex_j, level + 1, visited)

    visited[i][j] = False
    return cnt


h, w, k = map(int, input().split())
s = [list(input()) for _ in range(h)]
ans = 0

for i in range(h):
    for j in range(w):
        visited = [[False for _ in range(w)] for __ in range(h)]
        ans += dfs(i, j, 0, visited)

print(ans)
