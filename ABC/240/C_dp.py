# fmt: off
from collections import *
from itertools import *
import bisect, copy, heapq, math, numpy, string, queue
import sys
from functools import lru_cache

def I(): return int(sys.stdin.readline().rstrip()) # 数値
def LI(): return list(map(int, sys.stdin.readline().rstrip().split())) # 数値リスト
def S(): return sys.stdin.readline().rstrip() # 文字列
def LS(): return list(sys.stdin.readline().rstrip().split()) # 文字列リスト
def yes_no(b): return "Yes" if b else "No"

sys.setrecursionlimit(10**8)
mod = 998244353
# fmt: on

n, x = LI()
ab = [LI() for _ in range(n)]

dp = [[False for _ in range(x + 1)] for _ in range(n + 1)]
dp[0][0] = True

for i in range(n):
    for j in range(x):
        a, b = ab[i]
        if dp[i][j]:
            if j + a <= x:
                dp[i + 1][j + a] = True
            if j + b <= x:
                dp[i + 1][j + b] = True

print(yes_no(dp[n][x]))
