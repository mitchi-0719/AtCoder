# fmt: off
from collections import *
from itertools import *
import bisect, copy, heapq, math, numpy, string, queue
from sortedcontainers import *
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

n = I()
a = [LI() for _ in range(n)]
m = I()
xy = set([tuple(i - 1 for i in LI()) for _ in range(m)])

ans = inf
for p in set(permutations(range(n), n)):
    tmp = 0
    for i in range(n):
        tmp += a[p[i]][i]
        if i < n - 1 and ((p[i], p[i + 1]) in xy or (p[i + 1], p[i]) in xy):
            break
    else:
        ans = min(ans, tmp)

print(ans if ans != inf else -1)
