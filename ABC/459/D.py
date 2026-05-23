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

t = I()

for _ in range(t):
    d = defaultdict(int)
    s = S()
    n = len(s)

    for si in s:
        d[si] += 1

    if max(d.values()) > math.ceil(n / 2):
        print(no)
        continue

    print(yes)

    heap = [-i for i in d.values()]
    d_c = defaultdict(set)

    for k, v in d.items():
        d_c[v].add(k)

    heapq.heapify(heap)
    prev_c = ""
    push_n = 0
    for i in range(n):
        if i != 0:
            n_ = heapq.heapreplace(heap, -push_n) * -1
        else:
            n_ = heapq.heappop(heap) * -1

        c = d_c[n_].pop()
        if prev_c == c:
            _c = c
            c = d_c[n_].pop()
            d_c[n_].add(_c)

        print(c, end="")
        push_n = n_ - 1
        prev_c = c
        d_c[push_n].add(c)

    print()

"""
AC


"""
