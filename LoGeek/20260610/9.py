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

H, W, D = LI()
A = [LI() for _ in range(H)]
idx = [()] * (H * W)
for i in range(H):
    for j in range(W):
        idx[A[i][j] - 1] = (i, j)

acc = [[0] for _ in range(D)]

for k in range(D):
    for i in range(k + D, H * W, D):
        x1, y1 = idx[i - D]
        x2, y2 = idx[i]
        prev = acc[k][-1]
        acc[k].append(prev + abs(x1 - x2) + abs(y1 - y2))

Q = I()
for _ in range(Q):
    L, R = LI()
    i = (L - 1) % D
    print(acc[i][(R - 1) // D] - acc[i][(L - 1) // D])

"""
AC

Dが固定だから、遷移の流れは一定。
遷移の重みをmod Dごとに持っておき、それの累積和で高速に計算が可能。
"""
