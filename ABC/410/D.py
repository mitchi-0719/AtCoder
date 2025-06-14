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


def dfs(cur, bef, goal, ans):
    if cur == goal:
        return ans

    if len(g[cur]) == 1:
        return -1

    res = float("inf")
    for nex, w in g[cur]:
        if nex == bef:
            continue
        v = dfs(nex, cur, goal, ans ^ w)
        if v == -1:
            continue
        res = min(res, v)

    return res


n, m = LI()
g = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, w = LI()
    g[a].append((b, w))

st_v = dfs(1, None, n, 0)
gl_vs = []
for nex, w in g[-1]:
    gl_vs.append(dfs(nex, n, n, w))

print(gl_vs)
