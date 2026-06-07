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
def LI(): return list(map(int, sys.stdin.readline().rstrip().split())) # 数値リスト
def S(): return sys.stdin.readline().rstrip() # 文字列
def LS(): return list(sys.stdin.readline().rstrip().split()) # 文字列リスト
def yes_no(b): return yes if b else no
def sigma(n): (n * (n + 1)) // 2


dir8 = [(-1,-1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]
dir4 = [(0, -1), (1, 0),(0, 1), (-1, 0)]
# fmt: on

N, M = LI()
A = sorted(LI())
B = sorted(LI())

ab, nm = zip(*sorted(zip(A + B, [True] * N + [False] * M)))

ans = 0
s = 0
c = 0

for x, b in zip(ab, nm):
    if b:
        s += x
        c += 1
    else:
        ans += max(0, (x * c - s)) % mod

ab, nm = zip(*sorted(zip(A + B, [True] * N + [False] * M), reverse=True))

s = 0
c = 0

for x, b in zip(ab, nm):
    if b:
        s += x
        c += 1
    else:
        ans += max(0, (s - x * c)) % mod

print(ans % mod)

"""
解説AC

数直線で並べて、イメージで解いてみるとわかりやすい
"""
