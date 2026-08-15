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

N = I()
tlr = [LI() for _ in range(N)]

cnt = 0
for i in range(N - 1):
    for j in range(i + 1, N):
        if i == j:
            continue

        t1, l1, r1 = tlr[i]
        t2, l2, r2 = tlr[j]

        if t1 == 1:
            pass
        elif t1 == 2:
            r1 += 1
        elif t1 == 3:
            l1 -= 1
        elif t1 == 4:
            l1 -= 1
            r1 += 1

        if t2 == 1:
            pass
        elif t2 == 2:
            r2 += 1
        elif t2 == 3:
            l2 -= 1
        elif t2 == 4:
            l2 -= 1
            r2 += 1

        if l1 == l2:
            cnt += 1
        elif l1 < l2:
            cnt += 1 if r1 >= l2 else 0
        elif l1 > l2:
            cnt += 1 if r2 >= l1 else 0

        print(l1, r1, l2, r2)

print(cnt)
