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
def LI(): return list(map(int, sys.stdin.readline().rstrip().split())) # 数値リスト
def S(): return sys.stdin.readline().rstrip() # 文字列
def LS(): return list(sys.stdin.readline().rstrip().split()) # 文字列リスト
def yes_no(b): return yes if b else no
def sigma(n): (n * (n + 1)) // 2


dir8 = [(-1,-1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]
dir4 = [(0, -1), (1, 0),(0, 1), (-1, 0)]
# fmt: on

n, q = LI()
f = [[False] * n for _ in range(n)]

for _ in range(q):
    [t, *other] = LI()

    if t == 1:
        a, b = other
        a -= 1
        b -= 1

        f[a][b] = True
    elif t == 2:
        a = other[0]
        a -= 1

        for i in range(n):
            if f[i][a]:
                f[a][i] = True

    else:
        a = other[0]
        a -= 1

        x = []
        for xi in range(n):
            if f[a][xi]:
                x.append(xi)

        for i in x:
            for j in range(n):
                if f[i][j]:
                    f[a][j] = True


for i in range(n):
    for j in range(n):
        print("Y" if f[i][j] else "N", end="")
    print()
