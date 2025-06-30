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


def get_angle(a, b):
    return (180 * (b - a) + 180 * a * 2) % (180 * n)


n, m = LI()

d = defaultdict(int)
for _ in range(m):
    a, b = LI()
    angle = get_angle(a, b)
    d[angle] += 1

total = m * (m - 1) // 2
print(total - sum([(i * (i - 1)) // 2 for i in d.values()]))
