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
yes = "Yes"
no = "No"

dir8 = [(-1,-1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]
dir4 = [(0, -1), (1, 0),(0, 1), (-1, 0)]

# fmt: on

n = I()
a = LI()
g = [[] for _ in range(n)]

for _ in range(n - 1):
    u, v = LI()
    u, v = u - 1, v - 1
    g[u].append(v)
    g[v].append(u)

ans = defaultdict(bool)
d = defaultdict(int)
v = [False for _ in range(n)]


def dfs(cur, p):
    v[cur] = True
    f = d[a[cur]] >= 1

    if d[a[cur]] >= 1 or p >= 1:
        ans[cur] = True
        p += 1 if d[a[cur]] >= 1 else 0

    d[a[cur]] += 1
    for nex in g[cur]:
        if v[nex]:
            continue
        dfs(nex, p)

    d[a[cur]] -= 1
    p -= 1 if f else 0


dfs(0, 0)

for i in range(n):
    print(yes_no(ans[i]))


"""
[解説AC]


現在のノードじゃなくて、パス内のノードで重複があるかなのを読み間違えてた...
理解してしまえば実装はそんなに重くない。

dfsで1から探索していき、
入るときにdictの現在の値を加算する。もし、dictの値が1以上の場合にはペア数pを加算する
出るときにdictの現在の値を減算する。もし、入ったときのdictの値が1以上の場合にはペア数pを減算する
"""
