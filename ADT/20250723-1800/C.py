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

dir = [(1, 0), (0, -1), (-1, 0), (0, 1)]

n = I()
t = S()
dir_i = 0
x = 0
y = 0

for ti in t:
    if ti == "S":
        x += dir[dir_i % 4][0]
        y += dir[dir_i % 4][1]
    else:
        dir_i += 1

print(x, y)
