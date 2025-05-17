# fmt: off
from collections import *
from itertools import *
import bisect, copy, heapq, math, numpy, string, queue
import sys

def I(): return int(sys.stdin.readline().rstrip()) # 数値
def LI(): return list(map(int, sys.stdin.readline().rstrip().split())) # 数値リスト
def S(): return sys.stdin.readline().rstrip() # 文字列
def LS(): return list(sys.stdin.readline().rstrip().split()) # 文字列リスト
def yes_no(b): return "Yes" if b else "No"

sys.setrecursionlimit(10**8)
mod = 998244353
# fmt: on

h, w, n = LI()

dx = defaultdict(set)
dy = defaultdict(set)

for _ in range(n):
    x, y = LI()
    dx[x].add((x, y))
    dy[y].add((x, y))


q = I()
for _ in range(q):
    t, p = LI()
    ans = 0
    if t == 1:
        ans += len(dx[p])
        for x, y in dx[p]:
            dy[y].remove((x, y))
        dx[p] = []
    else:
        ans += len(dy[p])
        for x, y in dy[p]:
            dx[x].remove((x, y))
        dy[p] = []

    print(ans)
