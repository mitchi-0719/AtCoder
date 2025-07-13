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


def calc(a, b):
    ab = sum([ai * bi for ai, bi in zip(a, b)])
    an = math.sqrt(sum([ai**2 for ai in a]))
    bn = math.sqrt(sum([bi**2 for bi in b]))
    if an == 0 or bn == 0:
        return 0

    return math.acos(ab / (an * bn))


t = I()
l, x, y = LI()
q = I()

for _ in range(q):
    e = I() % t
    if e == 0:
        print(calc([0, 0, 0], [x, y, 0]))
    elif e < t / 2:
        p = l / (t / 2 / e)
        print(calc([0, -p, p], [x, y, 0]))
    else:
        e = e - t / 2
        p = l / (t / 2 / e)
        print(calc([0, p, p], [x, y, 0]))
