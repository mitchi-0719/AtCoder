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
A = LI()

g = [[] for _ in range(N + 1)]
for i in range(N):
    g[i + 1].append(A[i])


def color_dfs(g, color, parent, u):  # 閉路検索&閉路復元
    color[u] = 1  # 処理中にする

    for v in g[u]:
        if color[v] == 1:  # 閉路発見
            # 閉路復元処理
            cycle = []
            cur = u
            cycle.append(v)
            while cur != v:
                cycle.append(cur)
                cur = parent[cur]
            cycle.append(v)
            cycle.reverse()  # 順方向に直す
            return cycle

        # 処理完了（黒）は無視
        elif color[v] == 2:
            continue

        # 未訪問（白）の場合は再帰的に探索
        parent[v] = u
        result = color_dfs(g, color, parent, v)
        if result:
            return result
        parent[v] = -1

    # 処理完了（黒）にする
    color[u] = 2
    return []


color = [0] * (N + 1)
parent = [-1] * (N + 1)

for i in range(N):
    j = i + 1
    if color[j] == 0:
        result = color_dfs(g, color, parent, j)
        if result != []:
            print(len(result) - 1)
            print(*(result[:-1]))
            break

"""
AC

Color DFSで閉路探索をして終わり
"""
