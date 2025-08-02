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

n, m = LI()
s = [S() for _ in range(n)]
st = [set([j for j in range(m) if s[i][j] == "o"]) for i in range(n)]

for i in range(1, m + 1):
    p = combinations(range(n), i)
    for pi in p:
        tmp = set()
        for j in pi:
            for k in st[j]:
                tmp.add(k)

        if len(tmp) == m:
            print(i)
            exit()
