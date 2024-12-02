def dfs(i, j, level, visited):
    print(i, j, level, visited)
    if visited[i][j] or s[i][j] == "#":
        return 0

    visited[i][j] = True
    if level == k:
        return 1

    move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    cnt = 0
    for dx, dy in move:
        nex_i = i + dy
        nex_j = j + dx
        if 0 <= nex_i < h and 0 <= nex_j < w:
            cnt += dfs(nex_i, nex_j, level + 1, visited[:])

    return cnt


h, w, k = map(int, input().split())
s = [list(input()) for _ in range(h)]
ans = 0

for i in range(h):
    for j in range(w):
        visited = [[False for _ in range(w)] for __ in range(h)]
        ans += dfs(i, j, 0, visited)

print(ans)
