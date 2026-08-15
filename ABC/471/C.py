# fmt: off
from collections import *
from itertools import *
import bisect, copy, heapq, math,  string, queue
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

p, m = [], []
for ai in LI():
    if ai < 0:
        m.append(ai)
    else:
        p.append(ai)

ans = 0
m.sort()
p.sort(reverse=1)

cur = 0
mi = -inf
pi = inf

while 1:
    if mi == -inf and len(m) != 0:
        mi = m.pop()

    if pi == inf and len(p) != 0:
        pi = p.pop()

    if mi == -inf and pi == inf:
        break

    if abs(cur - mi) <= abs(cur - pi):
        ans += abs(cur - mi)
        cur = mi
        mi = -inf
    else:
        ans += abs(cur - pi)
        cur = pi
        pi = inf

print(ans)
