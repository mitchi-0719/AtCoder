# fmt: off
from collections import *
from itertools import *
import bisect, copy, heapq, math, string, queue
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


def int_to_str(n, L):
    return ["0"] * max(0, L - len(str(n))) + [s for s in str(n)]


def str_to_int(s):
    return int("".join(s))


def solve():
    a, L = LI()

    if a == L == 0:  # 終了条件
        return 1

    d = defaultdict(lambda: -1)

    i = 0
    ai = a
    d[ai] = 0
    while 1:
        a_min = str_to_int(sorted(int_to_str(ai, L)))
        a_max = str_to_int(sorted(int_to_str(ai, L), reverse=True))
        ai = a_max - a_min

        if d[ai] != -1:
            print(d[ai], ai, i - d[ai] + 1)
            return

        i += 1
        d[ai] = i


while not solve():
    ...
