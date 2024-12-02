import math

n = int(input())
date = [list(map(int, input().split())) for _ in range(n)]

q = int(input())
for _ in range(q):
    t, d = map(int, input().split())
    q, r = date[t - 1]

    n = math.ceil((d - r) / q)

    print(q * n + r)
