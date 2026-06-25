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

N = I()
C = LI()
G = [[] for _ in range(N)]

for _ in range(N - 1):
    A, B = LI()
    A -= 1
    B -= 1

    G[A].append(B)
    G[B].append(A)

ans = [0]


def dfs(prev, cur, ans, s):
    for v in G[cur]:
        if v == prev:
            continue

        c = C[v]
        if c not in s:
            ans.append(v)
        s.add(c)
        dfs(cur, v, ans, s)
        s.remove(c)


dfs(-1, 0, ans, SortedList([C[0]]))

for a in sorted(ans):
    print(a + 1)

"""
AC

マルチセットとかdictを使ってこれまでの数を数えればよき
"""
