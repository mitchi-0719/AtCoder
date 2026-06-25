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

Q = I()
queue_x = deque()
queue_c = deque()

for _ in range(Q):
    [t, *q] = LI()

    if t == 1:
        x, c = q
        queue_x.append(x)
        queue_c.append(c)
    else:
        c = q[0]
        s = 0
        while queue_c:
            if queue_c[0] <= c:
                p = queue_c.popleft()
                x = queue_x.popleft()
                c -= p
                s += p * x
            else:
                queue_c[0] -= c
                s += queue_x[0] * c
                break
        print(s)

"""
AC

dequeを使ってランレングス圧縮的な感じでデータを持っておくと行ける。
（圧縮しないと間に合わない気がする）
"""
