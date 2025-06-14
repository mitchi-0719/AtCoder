# fmt: off
from collections import *
from itertools import *
import bisect, copy, heapq, math, numpy, string, queue
import sys

def I(): return int(sys.stdin.readline().rstrip()) # 数値
def LI(): return list(map(int, sys.stdin.readline().rstrip().split())) # 数値リスト
def S(): return sys.stdin.readline().rstrip() # 文字列
def LS(): return list(sys.stdin.readline().rstrip().split()) # 文字列リスト
def yes_no(b): return "Yes" if b else "No"

sys.setrecursionlimit(10**8)
mod = 998244353
# fmt: on

n, h, m = LI()
ab = [LI() for _ in range(n)]

dp = [[-1] * (m + 1) for _ in range(n + 1)]

dp[0][m] = h

for i in range(1, n + 1):
    a, b = ab[i - 1]
    for j in range(m + 1):
        dp[i][j] = max(dp[i - 1][j] - a, dp[i - 1][j + b] if j + b < m + 1 else -1, -1)


for i, dp_i in enumerate(dp):
    if max(dp_i) == -1:
        print(i - 1)
        exit()

print(n)
