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

N, C = LI()
abc = [LI() for _ in range(N)]
l = []

for a, b, c in abc:
    l.append((a, c))
    l.append((b + 1, -c))

l = sorted(l, key=lambda x: [x[0], -x[1]])
m = len(l)
acc = [l[0][1]]
idx = [l[0][0]]

for i in range(1, m):
    t, v = l[i]
    if idx[-1] == t:
        acc[-1] += v
    else:
        acc.append(acc[-1] + v)
        idx.append(t)

ans = 0
n = len(acc)
for i in range(n - 1):
    ans += min(C, acc[i]) * (idx[i + 1] - idx[i])

print(ans)

"""
AC

imos法とかイベントソートである時刻に対して足し上げて、Cと比較していずれかを足せば良い。
（時刻が10**9なので、座標圧縮等をする必要がある。）
"""
