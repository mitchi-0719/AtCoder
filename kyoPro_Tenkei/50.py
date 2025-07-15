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
mod = 10**9+7
inf = float("inf")
# fmt: on

n, l = LI()
dp = [0 for _ in range(n + 1)]
dp[0] = 1

for i in range(1, n + 1):
    if i >= l:
        dp[i] += dp[i - l]
    dp[i] += dp[i - 1]

print(dp[-1] % mod)
