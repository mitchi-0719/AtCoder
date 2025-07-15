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
a = LI()
b = LI()
c = LI()

ad = defaultdict(int)
bd = defaultdict(int)
cd = defaultdict(int)
m = 46

for i in range(m):
    ad[i] = 0
    bd[i] = 0
    cd[i] = 0


for ai, bi, ci in zip(a, b, c):
    ad[ai % m] += 1
    bd[bi % m] += 1
    cd[ci % m] += 1

ans = 0
for ak, av in ad.items():
    for bk, bv in bd.items():
        for ck, cv in cd.items():
            if (ak + bk + ck) % m == 0:
                ans += av * bv * cv

print(ans)
