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


def total(n):
    return (n * (n + 1)) // 2


memo = defaultdict(lambda: float("inf"))


def gcd(n, m):
    if m == 0:
        return n
    else:
        if memo[(n, m)] != float("inf"):
            return memo[(n, m)]

        memo[(n, m)] = gcd(m, n % m)
        return memo[(n, m)]


def lcm(n, m):
    return (n * m) // gcd(n, m)


n, a, b = LI()
s = total(n)

t_a = total(n // a) * a
t_b = total(n // b) * b
l = lcm(a, b)
t_ab = total(n // l) * l
print(s - t_a - t_b + t_ab)
