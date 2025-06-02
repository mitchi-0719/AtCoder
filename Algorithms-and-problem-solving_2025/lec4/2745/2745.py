import math


def solve():
    r0, w0, c, r = map(int, input().split())

    if r0 == w0 == c == r == 0:
        return 1

    print(max(0, math.ceil((c * w0 - r0) / r)))


while 1:
    if solve():
        break
