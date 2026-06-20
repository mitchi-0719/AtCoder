# fmt: off
from collections import *
from itertools import *
import bisect, copy, heapq, math, string, queue
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


def solve():
    n = I()

    if n == 0:  # 終了条件
        return 1

    w = LI()
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for ln in range(2, n + 1):
        for l in range(n - ln + 1):
            r = l + ln

            for i in range(l + 1, r):
                dp[l][r] = max(dp[l][r], dp[l][i] + dp[i][r])

            if dp[l + 1][r - 1] == ln - 2 and abs(w[l] - w[r - 1]) < 2:
                dp[l][r] = ln

    print(dp[0][n])


while not solve():
    ...
