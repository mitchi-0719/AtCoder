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

N, K = LI()
a = LI()

d = defaultdict(SortedList)

for i in range(N):
    d[i % K].add(a[i])

prev = -inf
for i in range(math.ceil(N / K)):
    for j in range(K):
        if len(d[j]) <= i:
            break

        if d[j][i] >= prev:
            prev = d[j][i]
        else:
            print(no)
            exit()

print(yes)

"""
AC

SortedListで逐次ソートしたけど、別にそれぞれ分けてソートしても同じ。
"""
