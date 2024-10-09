import math
import sys

sys.setrecursionlimit(10**8)

def dist(a, b, c, d):
    return math.sqrt((a-c)**2 + (b-d)**2)

def solve(before, visit):
    d = float("inf")
    change = False
    for i in range(n):
        if not visit[i]:
            change = True
            new_visit = [*visit]
            new_visit[i] = True
            d = min(d, 
                    solve((p[i][2], p[i][3]), new_visit) + dist(p[i][0], p[i][1], before[0], before[1])/s,
                    solve((p[i][0], p[i][1]), new_visit) + dist(p[i][2], p[i][3], before[0], before[1])/s)

    return d if change else 0

n, s, t = map(int, input().split())
p = []

ans = 0
start = float("inf")

for i in range(n):
    p.append(list(map(int, input().split())))
    ans += dist(*p[i]) / t

print(ans + solve((0, 0), [False for _ in range(n)]))