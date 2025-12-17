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

n, m = LI()
g = [[] for _ in range(n)]
d = [0] * n

for _ in range(m):
    x, y = LI()
    g[x - 1].append(y - 1)
    d[y - 1] += 1

src = deque()
l = 0
for i in range(n):
    if d[i] == 0:
        src.append(i)

while len(src) > 0:
    for _ in range(len(src)):
        i = src.popleft()
        for j in g[i]:
            d[j] -= 1
            if d[j] == 0:
                src.append(j)
    l += 1

print(l - 1)

"""
解説見てACしたからもっかいちゃんと解く。
1. ソースとなる頂点を探す。
2. ソース頂点のすべての隣接の頂点の入次数を1下げる
3. 1に戻って繰り返す。ソース頂点が0になったら処理が終了。それまでにかかった回数-1が最長パスにあたる。
"""
