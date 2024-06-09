n = int(input())
t, x, y = [0], [0], [0]

for i in range(n):
    ti, xi, yi = map(int, input().split())
    t.append(ti)
    x.append(xi)
    y.append(yi)


def dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


for i in range(1, n + 1):
    d = dist(x[i - 1], y[i - 1], x[i], y[i])
    _t = t[i] - t[i - 1]
    if _t < d or (_t - d) % 2 != 0:
        print("No")
        exit()

print("Yes")
