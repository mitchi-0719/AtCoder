# fmt: off
from collections import *
from itertools import *
import bisect, copy, heapq, math, numpy, string, queue
from sortedcontainers import *
from functools import lru_cache
import sys
from pprint import pprint

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

t = I()


def solve():
    n, m = LI()
    g = defaultdict(set)
    uv = [LI() for _ in range(m)]

    w = I()
    s = [[]] + [[True if si == "o" else False for si in S()] for _ in range(n)]

    states = n * w

    for u, v in uv + [[i, i] for i in range(1, n + 1)]:
        for d in range(w):
            prev = s[u]
            nex = s[v]
            if prev[d] and nex[(d + 1) % w]:
                g[u * w + d].add(v * w + (d + 1) % w)

            prev = s[v]
            nex = s[u]
            if prev[d] and nex[(d + 1) % w]:
                g[v * w + d].add(u * w + (d + 1) % w)

    def color_dfs(g, color, u):
        color[u] = 1  # 処理中にする

        for v in g[u]:
            if color[v] == 1:  # 閉路発見
                return True

            # 処理完了（黒）は無視
            elif color[v] == 2:
                continue

            # 未訪問（白）の場合は再帰的に探索
            if color_dfs(g, color, v):
                return True

        # 処理完了（黒）にする
        color[u] = 2
        return False

    color = defaultdict(int)
    for i in range(1, n + 1):
        key = i * w
        if len(g[key]) != 0 and color[key] == 0:
            if color_dfs(g, color, key):
                print(yes)
                return

    print(no)


for _ in range(t):
    solve()

"""
AC
(地点, 曜日)のグラフの有向グラフを作成して色付きDFSで閉路の探索をしている。
日付をタプルで持つと検索に時間がかかるから、数値として持つようにして高速化をした。
"""
