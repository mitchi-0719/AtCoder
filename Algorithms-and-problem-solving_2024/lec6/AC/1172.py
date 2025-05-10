import math
import bisect

p = []
m = 123456
for i in range(2, m * 2 + 1):
    judge = True
    for j in range(2, int(math.sqrt(i) + 1)):
        if i % j == 0:
            judge = False
            break
    if judge:
        p.append(i)


def solve(n):
    i1 = bisect.bisect(p, n)
    i2 = bisect.bisect(p, 2 * n)
    print(i2 - i1)


while True:
    n = int(input())
    if n == 0:
        exit()
    solve(n)
