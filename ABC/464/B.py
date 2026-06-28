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

H, W = LI()
C = [SI() for _ in range(H)]
d = [0] * 4

for i in range(H):
    f = True
    for j in range(W):
        if C[i][j] == "#":
            f = False
            break

    if not f:
        d[0] = i
        break

for j in range(W):
    f = True
    for i in range(H):
        if C[i][j] == "#":
            f = False
            break

    if not f:
        d[1] = j
        break

for i in range(H):
    f = True
    for j in range(W):
        if C[-(i + 1)][j] == "#":
            f = False
            break

    if not f:
        d[2] = i
        break

for j in range(W):
    f = True
    for i in range(H):
        if C[i][-(j + 1)] == "#":
            f = False
            break

    if not f:
        d[3] = j
        break

for i in range(d[0], H - d[2]):
    for j in range(d[1], W - d[3]):
        print(C[i][j], end="")
    print()
