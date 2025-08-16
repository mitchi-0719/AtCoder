# fmt: off
from collections import *
from itertools import *
import bisect, copy, heapq, math, numpy, string, queue
from sortedcontainers import *
from functools import lru_cache
import sys

def I(): return int(sys.stdin.readline().rstrip()) # 数値
def LI(): return list(map(int, sys.stdin.readline().rstrip().split())) # 数値リスト
def S(): return sys.stdin.readline().rstrip() # 文字列
def LS(): return list(sys.stdin.readline().rstrip().split()) # 文字列リスト
def yes_no(b): return "Yes" if b else "No"
def print_nobreak(t, end=""): print(t, end=end)

sys.setrecursionlimit(10**8)
mod = 998244353
inf = float("inf")
# fmt: on

n = I()
a = [list(S()) for _ in range(n)]

d = defaultdict(set)

dirs = [(0, 1), (1, 0), (-1, 0), (0, -1), (-1, -1), (1, 1), (1, -1), (-1, 1)]

for i in range(n):
    for j in range(n):
        d[a[i][j]].add((i, j))

mx = max(d.keys())
ans = 0


def check(x, y, dx, dy):
    tmp = ""
    for i in range(n):
        tmp += a[(x + dx * i) % n][(y + dy * i) % n]
    return int(tmp)


for x, y in d[mx]:
    for dx, dy in dirs:
        ans = max(ans, check(x, y, dx, dy))

print(ans)
