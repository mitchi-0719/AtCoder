# fmt: off
from collections import *
from itertools import *
import bisect, copy, heapq, math, numpy, string, queue
import sys
from functools import lru_cache

def I(): return int(sys.stdin.readline().rstrip()) # 数値
def LI(): return list(map(int, sys.stdin.readline().rstrip().split())) # 数値リスト
def S(): return sys.stdin.readline().rstrip() # 文字列
def LS(): return list(sys.stdin.readline().rstrip().split()) # 文字列リスト
def yes_no(b): return "Yes" if b else "No"

sys.setrecursionlimit(10**8)
mod = 998244353
# fmt: on

n, x = LI()
ab = [LI() for _ in range(n)]
d = {}


def solve(y, i):
    if d.get((y, i)) != None:
        return d.get((y, i))

    if i == n:
        if x == y:
            return True
        else:
            return False

    a, b = ab[i]

    if y > x:
        return False

    d[(y + a, i + 1)] = solve(y + a, i + 1)
    d[(y + b, i + 1)] = solve(y + b, i + 1)

    return d[(y + a, i + 1)] or d[(y + b, i + 1)]


print(yes_no(solve(0, 0)))
