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

s = S()
l = len(s)
dp = [[0] * (l) for _ in range(l)]

if len(s) % 2 == 1 or s[0] == ")":
    print(0)
    exit()

if s[0] == "(":
    dp[0][1] = 1
if s[0] == "?":
    dp[0][0] = dp[0][1] = 1

for i in range(0, l - 1):
    for j in range(l):
        if dp[i][j] != 0:
            if s[i + 1] == "(":
                if j + 1 < l:
                    dp[i + 1][j + 1] += dp[i][j] % mod
            elif s[i + 1] == ")":
                if j - 1 >= 0:
                    dp[i + 1][j - 1] += dp[i][j] % mod
            else:
                if j - 1 >= 0:
                    dp[i + 1][j - 1] += dp[i][j] % mod
                if j + 1 < l:
                    dp[i + 1][j + 1] += dp[i][j] % mod

print(dp[-1][0] % mod)
