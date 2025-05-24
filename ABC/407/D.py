# fmt: off
from collections import *
from itertools import *
import bisect, copy, heapq, math, numpy, string, queue
import sys

def I(): return int(sys.stdin.readline().rstrip()) # 数値
def LI(): return list(map(int, sys.stdin.readline().rstrip().split())) # 数値リスト
def S(): return sys.stdin.readline().rstrip() # 文字列
def LS(): return list(sys.stdin.readline().rstrip().split()) # 文字列リスト
def yes_no(b): return "Yes" if b else "No"

sys.setrecursionlimit(10**8)
mod = 998244353
# fmt: on


def calc():
    ans = 0
    for i in range(h):
        for j in range(w):
            ans ^= 0 if t[i][j] else a[i][j]

    return ans


def encode(i, j):
    return i * w + j


def decode(n):
    return n // w, n % w


def solve(n):
    if n == h * w - 1:
        return calc()

    i, j = decode(n)
    mx = 0
    mx = max(mx, solve(n + 1))

    if t[i][j]:
        return mx

    if i + 1 != h:
        t[i][j] = t[i + 1][j] = True
        mx = max(mx, solve(n + 1))
        t[i][j] = t[i + 1][j] = False

    if j + 1 != w:
        t[i][j] = t[i][j + 1] = True
        mx = max(mx, solve(n + 1))
        t[i][j] = t[i][j + 1] = False

    return mx


h, w = LI()
a = [LI() for _ in range(h)]
t = [[False] * w for _ in range(h)]
s = 0

print(solve(0))
