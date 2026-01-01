# fmt: off
from collections import *
from itertools import *
import bisect, copy, heapq, math, numpy, string, queue
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


@lru_cache
def solve(i, j):
    if i == H:
        return 0

    mx = 0
    for k in range(-1, 2):
        if 0 <= j + k < W:
            mx = max(mx, solve(i + 1, j + k) + s[i][j])

    return mx


H, W = LI()
s = [LI() for _ in range(H)]

mx = 0
for j in range(W):
    mx = max(mx, solve(0, j))

print(mx)


# 未クリア
