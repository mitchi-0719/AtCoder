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
from atcoder.lazysegtree import LazySegTree


n, m = LI()
s = S()
t = S()
lr = [LI() for _ in range(m)]

INF = 1 << 63


def op(ele1, ele2):
    return min(ele1, ele2)


def mapping(func, ele):
    return func + ele


def composition(func_upper, func_lower):
    return func_upper + func_lower


e = INF
id_ = 0

seg = LazySegTree(op, e, mapping, composition, id_, [0 for _ in range(n)])
for l, r in lr:
    l -= 1
    seg.apply(l, r, 1)

for i in range(n):
    if seg.get(i) % 2 == 0:
        print_nobreak(s[i])
    else:
        print_nobreak(t[i])
print()
