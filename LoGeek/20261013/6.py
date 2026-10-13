# fmt: off
from collections import *
from itertools import *
import bisect, copy, heapq, math, numpy, string, queue
from sortedcontainers import *
from functools import lru_cache
import sys
from pprint import pprint

sys.setrecursionlimit(10**7)
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

S = SI()
Q = I()

d = deque(list(S))
rev = False

for _ in range(Q):
    [t, *q] = LS()
    if t == "1":
        rev = not rev
    else:
        f, c = q
        if f == "1":
            if rev:
                d.append(c)
            else:
                d.appendleft(c)
        else:
            if rev:
                d.appendleft(c)
            else:
                d.append(c)

print("".join(reversed(d) if rev else d))
