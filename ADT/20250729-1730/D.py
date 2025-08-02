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

n, q = LI()
lr = {"L": 0, "R": 1}
ans = 0

for _ in range(q):
    h, t = LS()
    t = int(t) - 1
    rev_i = lr["L"] if h == "R" else lr["R"]

    i = 0
    while 1:
        cur = (lr[h] + i) % n
        if cur == t:
            break
        if cur == rev_i:
            i = -1
            break

        i += 1

    if i >= 0:
        ans += i
        lr[h] = t
        continue

    i = 0
    while 1:
        cur = (lr[h] + i) % n
        if cur == t:
            break
        if cur == rev_i:
            i = -1
            break

        i -= 1

    ans += i * -1
    lr[h] = t

print(ans)
