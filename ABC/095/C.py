a, b, c, x, y = map(int, input().split())

ans = float("inf")

for ab in range(0, 10**6, 2):
    s = c * ab

    _x = x - ab // 2
    _y = y - ab // 2

    if 0 < _x:
        s += _x * a
    if 0 < _y:
        s += _y * b

    ans = min(ans, s)

print(ans)
