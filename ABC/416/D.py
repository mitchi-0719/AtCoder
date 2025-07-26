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


def solve():
    n, m = LI()
    a = LI()
    b = LI()

    a_mod = sorted([i % m for i in a])
    b_mod = sorted([i % m for i in b])
    a_dict = defaultdict(int)
    b_dict = defaultdict(int)

    ans = 0
    for ai, bi in zip(a_mod, b_mod):
        a_dict[ai] += 1
        b_dict[bi] += 1

    k = sorted(a_dict.keys())
    for i in k:
        if i == 0:
            j = 0
        else:
            j = m - i

        mn = min(a_dict[i], b_dict[j])
        a_dict[i] -= mn
        b_dict[j] -= mn

    a_list = []
    b_list = []

    for k, v in a_dict.items():
        a_list += [k] * v

    for k, v in b_dict.items():
        b_list += [k] * v

    for ai, bi in zip(sorted(a_list), reversed(b_list)):
        ans += (ai + bi) % m
        print((ai + bi) % m)
    print(a_list)
    print(list(reversed(b_list)))
    print(ans)


t = I()
for _ in range(t):
    solve()
