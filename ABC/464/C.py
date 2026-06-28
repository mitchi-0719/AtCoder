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

N, M = LI()
ADB = sorted([LI() for _ in range(N)], key=lambda x: x[1])

dic = defaultdict(list)
cnt = defaultdict(int)

for a, d, b in ADB:
    if d == 1:
        cnt[b] += 1
    else:
        cnt[a] += 1
        if a != b:
            dic[d - 1].append((a, b))

c = len(cnt.keys())

for i in range(M):
    for bef, aft in dic[i]:
        if cnt[bef] == 1:
            c -= 1
        if cnt[aft] == 0:
            c += 1

        cnt[bef] -= 1
        cnt[aft] += 1

    print(c)


"""
AC

各時間における増減をdictで管理して持っておいて、時間ごとに計算しながらやればいい
"""
