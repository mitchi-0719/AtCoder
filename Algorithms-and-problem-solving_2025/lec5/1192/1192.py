import math


def tax(p, t):
    return p * (100 + t) // 100


def solve():
    x, y, s = map(int, input().split())
    if x == y == s == 0:
        return 1

    ans = 0
    for i in range(1, s):
        for j in range(1, s):
            if tax(i, x) + tax(j, x) == s:
                ans = max(ans, tax(i, y) + tax(j, y))

    print(ans)


while not solve():
    ...
