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

H, W = LI()
c = [LI() for _ in range(H)]

dp = [[0 for _ in range(W + 1)] for _ in range(H + 1)]

for i in range(H):
    for j in range(W):
        if c[i][j] == 0:
            # c[i][j]が0の時、最小の正方形の長さは1
            # もし、そこを右下としたときの上、左、左上の3箇所が同値であれば、その値+1がc[i][j]を右下と見たときの最大の正方形のサイズとなる
            dp[i + 1][j + 1] = min(dp[i][j], dp[i + 1][j], dp[i][j + 1]) + 1

ans = 0
for i in range(H + 1):
    ans = max(ans, *dp[i])

print(ans**2)
