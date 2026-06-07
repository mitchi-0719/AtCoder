# fmt: off
from collections import *
from itertools import *
import bisect, copy, heapq, math, numpy, string, queue
from sortedcontainers import *
from functools import lru_cache
import sys
from pprint import pprint
from atcoder.lazysegtree import LazySegTree

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
X = LI()
P = LI()


def op(ele1, ele2):
    return ele1 + ele2


def mapping(func, ele):
    return func + ele


def composition(func_upper, func_lower):
    return func_upper + func_lower


e = 0
id_ = 0

segTree = LazySegTree(op, e, mapping, composition, id_, P)

Q = I()

for _ in range(Q):
    L, R = LI()
    li = bisect.bisect_left(X, L)
    ri = bisect.bisect(X, R)

    print(segTree.prod(li, ri))

"""
AC

セグ木で範囲を見てやるだけ
セグ木の作り方ちゃんと理解しないと
"""
