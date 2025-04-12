from collections import defaultdict

h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]
d = defaultdict(bool)


def dfs(i, j):
    if d[a[i][j]]:
        return 0

    if (i + 1, j + 1) == (h, w):
        return 1

    d[a[i][j]] = True
    cnt = 0
    if i + 1 < h:
        cnt += dfs(i + 1, j)
    if j + 1 < w:
        cnt += dfs(i, j + 1)
    d[a[i][j]] = False

    return cnt


print(dfs(0, 0))
