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

n = I()
d = defaultdict(SortedList)
f_max = SortedList()
f_set = set()
ans = 0

for _ in range(n):
    f, s = LI()
    d[f].add(s)
    f_set.add(f)

for f in f_set:
    f_max.add(d[f][-1])

if len(f_max) >= 2:
    ans = f_max[-1] + f_max[-2]

for v in d.values():
    if len(v) >= 2:
        ans = max(ans, v[-1] + v[-2] // 2)

print(ans)
