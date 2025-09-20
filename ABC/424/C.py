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
mod = 998244353
inf = float("inf")
# fmt: on


n = I()
g = [[] for _ in range(n + 1)]

for i in range(n):
    a, b = LI()
    g[a].append(i + 1)
    g[b].append(i + 1)


def dfs(s):
    ok[s] = 1

    for v in g[s]:
        if ok[v]:
            continue

        dfs(v)


ok = [False for _ in range(n + 1)]
ok[0] = True
dfs(0)
print(sum(ok) - 1)
