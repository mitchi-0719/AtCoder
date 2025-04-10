"""これを2乗距離にしたら行けた
import math


def dist(x1, x2, y1, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


r, x, y = map(int, input().split())
d = dist(0, x, 0, y)

m = 0
ans = 0

while True:
    m += r
    ans += 1
    if abs(d - m) <= r:
        print(ans + 1)
        break
    if abs(d - m) <= r * 2:
        print(ans + 2)
        break
"""

r, x, y = map(int, input().split())
ds = x**2 + y**2

rs = r**2
ans = 0

if ds < rs:
    print(2)
else:
    while ans**2 * rs < ds:
        ans += 1
    print(ans)
