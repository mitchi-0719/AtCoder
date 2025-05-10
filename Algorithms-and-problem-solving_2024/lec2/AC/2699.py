# AC

import math


def solve(d, e):
    ans = float("inf")
    for x in range(d):
        y = d - x
        ans = min(ans, abs(math.sqrt(x**2 + y**2) - e))
    print(ans)


while True:
    d, e = map(int, input().split())
    if d == e == 0:
        exit()

    solve(d, e)
