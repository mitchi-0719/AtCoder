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

N = I()
dp = [[0] * 9 for _ in range(N)]

for j in range(9):
    dp[0][j] = 1

for i in range(1, N):
    for j in range(9):
        if j == 0:
            dp[i][j] = dp[i - 1][j] % mod + dp[i - 1][j + 1] % mod
        elif j == 8:
            dp[i][j] = dp[i - 1][j] % mod + dp[i - 1][j - 1] % mod
        else:
            dp[i][j] = (
                dp[i - 1][j] % mod + dp[i - 1][j + 1] % mod + dp[i - 1][j - 1] % mod
            )

print(sum(dp[-1]) % mod)

"""
AC

移動のパターンをDPテーブルで保持すりゃええ
"""
