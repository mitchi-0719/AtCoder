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
rc = []

x_max = 0
x_min = inf
y_max = 0
y_min = inf


for _ in range(n):
    r, c = LI()
    x_max = max(x_max, r)
    x_min = min(x_min, r)
    y_max = max(y_max, c)
    y_min = min(y_min, c)

dx = math.ceil((x_max - x_min) / 2)
dy = math.ceil((y_max - y_min) / 2)

print(max(dx, dy))
