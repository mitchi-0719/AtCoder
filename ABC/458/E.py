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

x1, x2, x3 = LI()

k = x2 + 1
ans = 0

x1, x3 = max(x3, x1), min(x3, x1)

for i in range(1, min(x1, k - 1) + 1):
    tmp = 1
    tmp *= math.comb(k, i) % mod
    tmp *= math.comb(x1 - 1, i - 1) % mod
    tmp *= math.comb(x3 + k - i - 1, k - i - 1) % mod

    ans += tmp % mod

print(ans)
