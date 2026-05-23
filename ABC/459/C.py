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
base = 0

l = SortedList([0] * n)

s = [0] * n
for _ in range(q):
    t, x = LI()
    x -= 1
    if t == 1:
        cur = s[x]
        s[x] += 1
        l.discard(cur)
        l.add(s[x])
        if l[0] != base:
            base += 1
    else:
        print(n - l.bisect_right(x + base))
