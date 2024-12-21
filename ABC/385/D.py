import bisect
from sortedcontainers import SortedSet
from collections import defaultdict

n, m, x, y = map(int, input().split())
xy = [list(map(int, input().split())) for _ in range(n)]
dx = defaultdict(SortedSet)
dy = defaultdict(SortedSet)
nx, ny = x, y


def is_in_range(start, end, x):
    if start < end:
        return start <= x <= end
    return end <= x <= start


for x, y in xy:
    dx[x].add(y)
    dy[y].add(x)

ans = 0
for _ in range(m):
    d, c = input().split()
    c = int(c)

    if d == "U":
        s = ny
        e = ny + c

        for i in range(len(dx[nx])):
            if is_in_range(s, e, dx[nx][i]):
                dyi = dx[nx][i]
                dx[nx].remove(dyi)
                dy[dyi].remove(nx)
                ans += 1
        ny += c

    elif d == "D":
        s = ny
        e = ny - c

        for i in range(len(dx[nx])):
            if is_in_range(s, e, dx[nx][i]):
                dyi = dx[nx][i]
                dx[nx].remove(dyi)
                dy[dyi].remove(nx)
                ans += 1

        ny -= c

    elif d == "L":
        s = nx
        e = nx - c

        for i in range(len(dy[ny])):
            if is_in_range(s, e, dy[ny][i]):
                dxi = dy[ny][i]
                dy[ny].remove(dxi)
                dx[dxi].remove(ny)
                ans += 1

        nx -= c

    elif d == "R":
        s = nx
        e = nx + c

        for i in range(len(dy[ny])):
            if is_in_range(s, e, dy[ny][i]):
                dxi = dy[ny][i]
                dy[ny].remove(dxi)
                dx[dxi].remove(ny)
                ans += 1

        nx += c


print(nx, ny, ans)
