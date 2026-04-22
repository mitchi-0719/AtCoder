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
yes = "Yes"
no = "No"

dir8 = [(-1,-1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]
dir4 = [(0, -1), (1, 0),(0, 1), (-1, 0)]

# fmt: on

n = I()
lr = sorted([LI() for _ in range(n)])

ans = []

l, r = lr[0]
for i in range(1, n):
    li, ri = lr[i]

    if r >= li:
        r = max(r, ri)
    else:
        ans.append((l, r))
        l, r = li, ri

ans.append((l, r))

for l, r in ans:
    print(l, r)


"""
解説AC

半開区間を逐一更新していくと出来るよねって感じ。
imos法でも出来る。
"""
