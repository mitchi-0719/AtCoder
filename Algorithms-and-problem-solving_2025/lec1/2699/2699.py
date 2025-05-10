import math


def solve():
    while True:
        d, e = map(int, input().split())

        if d == e == 0:
            return

        ans = float("inf")
        for di in range(d):
            x = di
            y = d - x

            ans = min(ans, abs(math.sqrt(x**2 + y**2) - e))

        print(ans)


solve()
