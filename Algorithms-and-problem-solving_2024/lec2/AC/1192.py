# AC

import math

while True:
    x, y, s = map(int, input().split())
    if x == y == s == 0:
        exit()

    ans = -1

    for i in range(1, s - 1):
        for j in range(1, s - 1):
            p1 = math.floor((i * (100 + x)) / 100)
            p2 = math.floor((j * (100 + x)) / 100)
            if p1 + p2 == s:
                _p1 = math.floor((i * (100 + y)) / 100)
                _p2 = math.floor((j * (100 + y)) / 100)
                ans = max(ans, _p1 + _p2)

    print(ans)
