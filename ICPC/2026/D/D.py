# fmt: off
from collections import *
from itertools import *
import bisect, copy, heapq, math, string, queue
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


def check(s, k, m):
    end = m * (s * 2 - m)
    return k <= end


def solve():
    s, k = LI()
    if s == k == 0:  # 終了条件
        return 1

    if s**2 + 1 == k:
        print(s)
    elif s**2 + 1 > k:
        l = 1
        r = s + 1
        m = (l + r) // 2
        while r - l >= 1:
            if not check(s, k, m):
                l = m + 1
            else:
                r = m

            m = (l + r) // 2
        row = l

        head = (row - 1) * (s * 2 - (row - 1)) + 1
        if head == k:
            print(s)
        else:
            if (k - head) % 2 == 1:
                print((k - head) // 2 + row)
            else:
                print(row)

    else:
        s2 = s * 2
        l = k - (s**2 + 2)
        if l % 2 == 0:
            print(s + l // (s2) + 1)
        else:
            print(l % s2 // 2 + 1)


while not solve():
    ...
