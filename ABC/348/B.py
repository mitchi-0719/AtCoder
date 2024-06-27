import math

n = int(input())
xy = []

for i in range(n):
    x, y = map(int, input().split())
    xy.append((x, y))


def calc(xy, i, j):
    return math.sqrt(pow(xy[i][0] - xy[j][0], 2) + pow(xy[i][1] - xy[j][1], 2))


for i in range(n):
    m = i
    for j in range(n):
        if i == j:
            continue
        d0 = calc(xy, i, m)
        dj = calc(xy, i, j)
        if d0 < dj:
            m = j
    print(m + 1)
