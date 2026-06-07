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

N = I()
A = [-1] + LI()
Q = I()

rep = -1
change = set([i + 1 for i in range(N)])
for _ in range(Q):
    t, *query = LI()

    if t == 1:
        [x] = query
        rep = x
        change = set()

    elif t == 2:
        i, x = query
        if i in change:
            A[i] += x
        else:
            A[i] = rep + x
            change.add(i)

    elif t == 3:
        [i] = query
        if i in change:
            print(A[i])
        else:
            print(rep)

"""
AC

変更をsetで管理しておいて、一括で変更しなくても良いようにするだけ
"""
