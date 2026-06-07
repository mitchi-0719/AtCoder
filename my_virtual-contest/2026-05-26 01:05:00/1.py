# fmt: off
from collections import *
from itertools import *
import bisect, copy, heapq, math, numpy, string, queue
from sortedcontainers import *
from functools import lru_cache
import sys
from pprint import pprint

sys.setrecursionlimit(10**8)
yes = "Yes"
no = "No"
mod = 998244353
inf = float("inf")

def I(): return int(sys.stdin.readline().rstrip()) # 数値
def LI(): return list(map(int, sys.stdin.readline().rstrip().split())) # 数値リスト
def S(): return sys.stdin.readline().rstrip() # 文字列
def LS(): return list(sys.stdin.readline().rstrip().split()) # 文字列リスト
def yes_no(b): return yes if b else no
def sigma(n): (n * (n + 1)) // 2


dir8 = [(-1,-1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]
dir4 = [(0, -1), (1, 0),(0, 1), (-1, 0)]
# fmt: on

N = I()
a = LI()

a_unique = sorted(set(a))
a_count = Counter(a)

ans = 1

if len(a_unique) == 1:
    print(N)
    exit()

if len(a_unique) == 2:
    if abs(a_unique[0] - a_unique[1]) <= 2:
        print(N)
        exit()
    else:
        print(max(a_count[a_unique[0]], a_count[a_unique[1]]))
        exit()

for i in range(1, len(a_unique) - 1):
    a1, a2, a3 = a_unique[i - 1], a_unique[i], a_unique[i + 1]

    if a3 - a1 <= 2:
        ans = max(ans, a_count[a1] + a_count[a2] + a_count[a3])

    elif a3 - a2 <= 2:
        ans = max(ans, a_count[a3] + a_count[a2])

    elif a2 - a1 <= 2:
        ans = max(ans, a_count[a2] + a_count[a1])

    else:
        ans = max(ans, a_count[a3], a_count[a2], a_count[a1])


print(ans)


"""
AC

たくさん条件分岐をしたけど、もっと簡単に行けるらしい
"""
