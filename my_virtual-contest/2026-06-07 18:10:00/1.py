# fmt: off
from collections import *
from itertools import *
import bisect, copy, heapq, math, numpy, string, queue
from sortedcontainers import *
from functools import lru_cache
import sys
from pprint import pprint

sys.setrecursionlimit(10**8)
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

H, W = LI()
a = [list(SI()) for _ in range(H)]
r = set()
c = set()

for i in range(H):
    for j in range(W):
        if a[i][j] == "#":
            break
    else:
        r.add(i)

for j in range(W):
    for i in range(H):
        if a[i][j] == "#":
            break
    else:
        c.add(j)

for i in range(H):
    if i in r:
        continue
    for j in range(W):
        if j in c:
            continue
        print(a[i][j], end="")

    print()

"""
AC

除外する行・列をsetに持っておいて参照する。
"""
