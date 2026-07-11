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
st = 1
ed = 2
ans = 0
prev = -1

while st < N and ed <= N:
    print(f"? {st} {ed}", flush=True)
    s = SI()
    if s == yes:
        if prev == no:
            ans += ed - st - 1
            st = ed
            ed += 1
        else:
            if ed == N:
                st += 1
            else:
                ed += 1
            ans += ed - st
    else:
        st += 1
    prev = s

print("!", ans, flush=True)
