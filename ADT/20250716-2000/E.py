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
s = list(S())
w = LI()

w, s = zip(*sorted(zip(w, s), key=lambda x: (-x[0], x[1]), reverse=True))
ans = s.count("1")
mx = ans
for si in s:
    if si == "1":
        ans -= 1
    else:
        ans += 1
    mx = max(ans, mx)

print(mx)
