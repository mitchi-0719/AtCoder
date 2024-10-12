import math


def dist(a, b, c, d):
    return math.sqrt((a - c) ** 2 + (b - d) ** 2)


n = int(input())

before = [0, 0]
ans = 0
for i in range(n):
    p = list(map(int, input().split()))
    ans += dist(*before, *p)
    before = p

p = [0, 0]
ans += dist(*before, *p)

print(ans)
