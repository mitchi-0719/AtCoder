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


def calc(e):
    theta = e / t * 2 * math.pi
    y = -l / 2 * math.sin(theta)
    z = l / 2 - math.cos(theta) * l / 2
    b = math.sqrt(X**2 + (Y - y) ** 2)

    return math.atan2(z, b) / math.pi * 180


t = I()
l, X, Y = LI()
q = I()
t2 = t / 2
t4 = t / 4
chokudai = [X, Y, 0]

for _ in range(q):
    e = I()
    print(calc(e))
