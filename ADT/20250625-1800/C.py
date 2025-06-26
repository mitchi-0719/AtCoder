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
def print_nobreak(t, end=""): print(t, end=end)

sys.setrecursionlimit(10**8)
mod = 998244353
# fmt: on


def dist(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1 / 2)


n, k = LI()
a = LI()
a_set = set(a)
xy = [LI() for _ in range(n)]

ans = 0
for i, [x, y] in enumerate(xy):
    buf = float("inf")
    for ai in a:
        ax, ay = xy[ai - 1]
        buf = min(buf, dist(x, y, ax, ay))
    ans = max(ans, buf)


print(ans)
