# fmt: off
from collections import *
from itertools import *
import bisect, copy, heapq, math, numpy, string, queue
from sortedcontainers import *
from functools import lru_cache
import sys
from atcoder.lazysegtree import LazySegTree

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


def op(n1, n2):
    return n1 + n2


def mapping(lazy_upper, data_lower):
    return data_lower + lazy_upper


def composition(lazy_upper, lazy_lower):
    return lazy_upper + lazy_lower


n = I()
a = LI()

mx = max(a)

lazy_segtree = LazySegTree(op, 0, mapping, composition, 0, [0] * (mx))

for ai in a:
    lazy_segtree.apply(0, ai, 1)

ans = []
over = 0
for i in range(mx):
    j = lazy_segtree.get(i) + over
    if j >= 10:
        over = j // 10
        j %= 10
    else:
        over = 0

    ans.append(str(j))

if over != 0:
    ans.append(str(over))

print("".join(ans[::-1]))
