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


s = S()

must = []
_any = []

for i in range(10):
    if s[i] == "o":
        must.append(str(i))
    elif s[i] == "?":
        _any.append(str(i))

if len(must) >= 5:
    print(0)
    exit()

ans = set()

for c in combinations((_any + must) * 4, 4 - len(must)):
    l = must + list(c)
    for p in permutations(l, 4):
        ans.add(p)

print(len(ans))

"""
AC

順列と組み合わせをごちゃごちゃやったらいけた。
絶対もっといい方法ある
"""
