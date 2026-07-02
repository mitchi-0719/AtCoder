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
S = [SI() for _ in range(N)]

sr = [0] * N
sc = [0] * N

for i in range(N):
    for j in range(N):
        if S[i][j] == "o":
            sr[i] += 1
            sc[j] += 1

ans = 0
for i in range(N):
    for j in range(N):
        if S[i][j] == "o":
            ans += (sr[i] - 1) * (sc[j] - 1)

print(ans)

"""
AC

1つピボットを決めて、その横と縦にあるoの数を使って組み合わせパターンを計算する
"""
