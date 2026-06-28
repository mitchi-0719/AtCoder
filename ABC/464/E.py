# fmt: off
from collections import *
from itertools import *
import bisect, copy, heapq, math, numpy, string, queue
from sortedcontainers import *
from functools import lru_cache
import sys
from pprint import pprint

sys.setrecursionlimit(10**7)
yes = "Yes"
no = "No"
mod = 998244353
inf = float("inf")

def I(): return int(sys.stdin.readline().rstrip()) # 数値
def F(): return float(sys.stdin.readline().rstrip()) # 小数値
def LI(): return list(map(int, sys.stdin.readline().rstrip().split())) # 数値リスト
def SI(): return sys.stdin.readline().rstrip() # 文字列
def LS(): return list(sys.stdin.readline().rstrip().split()) # 文字列リスト
def DL(init, n, m): return [[init for _ in range(m)] for __ in range(n)]
def yes_no(b): return yes if b else no
def sigma(n): return (n * (n + 1)) // 2


dir8 = [(-1,-1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]
dir4 = [(0, -1), (1, 0),(0, 1), (-1, 0)]
# fmt: on

H, W, Q = LI()
RCX = [LS() for _ in range(Q)]
RCX = [[int(r) - 1, int(c) - 1, x] for r, c, x in RCX]

b = [["" for _ in range(W)] for _ in range(H)]


def fill(r, c, x):
    for i in range(r, -1, -1):
        if b[i][c] != "":
            return
        d = 0
        for j in range(c, -1 + d, -1):
            if b[i][j] != "":
                d = j
                break
            b[i][j] = x


for r, c, x in reversed(RCX):
    fill(r, c, x)

fill(H - 1, W - 1, "A")

for bi in b:
    print("".join(bi))

"""
AC

後ろから順にに右下から左上方向にループをして進めていき、既に埋まっている領域を無視するようにうまくループする
"""
