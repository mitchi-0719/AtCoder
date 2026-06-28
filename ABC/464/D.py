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

T = I()


def solve():
    N = I()
    S = SI()
    X = LI()
    Y = LI()

    dp = [[0] * 2 for _ in range(N)]

    dp[0][0] = 0
    dp[0][1] = -X[0]

    for i in range(1, N):
        dp[i][0] = max(
            dp[i - 1][0] + (Y[i - 1] if S[i] == "S" and S[i - 1] == "R" else 0),
            dp[i - 1][1] + (Y[i - 1] if S[i] == "S" and S[i - 1] == "S" else 0),
        )

        dp[i][1] = max(
            dp[i - 1][0] + (Y[i - 1] if S[i] == "R" and S[i - 1] == "R" else 0) - X[i],
            dp[i - 1][1] + (Y[i - 1] if S[i] == "R" and S[i - 1] == "S" else 0) - X[i],
        )

    print(max(dp[-1]))


for _ in range(T):
    solve()

"""
AC

各曜日において、変更をするorしないのDPテーブルを組めば行ける
"""
