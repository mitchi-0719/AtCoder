import pprint


def dfs(m, w, h, d, i, xy, visited):
    if visited[i]:
        return

    visited[i] = True
    x, y = xy[i]
    for j in range(-d, d + 1):
        if j + x < 0 or w <= j + x or m[y][x + j] == -1:
            continue
        dfs(m, w, h, d, m[y][x + j], xy, visited)

    for j in range(-d, d + 1):
        if j + y < 0 or h <= j + y or m[y + j][x] == -1:
            continue
        dfs(m, w, h, d, m[y + j][x], xy, visited)


def solve():
    while True:
        w, h, n, d, b = map(int, input().split())

        if (w, h, n, d, b) == (0, 0, 0, 0, 0):
            return

        xy = [list(map(int, input().split())) for _ in range(n)]
        xy = [[x - 1, y - 1] for x, y in xy]

        m = [[-1 for _ in range(w)] for __ in range(h)]

        for i in range(n):
            x, y = xy[i]
            m[y][x] = i
        visited = [False for _ in range(n)]

        dfs(m, w, h, d, b - 1, xy, visited)
        print(len([v for v in visited if v]))


solve()
