# fmt: off
from collections import *
from itertools import *
import bisect, copy, heapq, math, numpy, string, queue
from sortedcontainers import *
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


def solve():
    n = I()
    a = LI()
    if len(set(a)) == 1:
        return True

    p_cnt = a.count(a[0])
    n_cnt = a.count(-a[0])
    if p_cnt + n_cnt == n and min(p_cnt, n_cnt) == n // 2:
        return True

    b = sorted(a, key=lambda x: abs(x), reverse=True)

    for i in range(1, n - 1):
        if b[i] ** 2 != b[i - 1] * b[i + 1]:
            return False

    return True


t = I()
for _ in range(t):
    print(yes_no(solve()))
