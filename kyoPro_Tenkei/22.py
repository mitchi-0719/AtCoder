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

# nとmの最大公約数は m と (n/mのあまり)の最大公約数に等しい

memo = defaultdict(lambda: float("inf"))


def gcd(n, m):
    if m == 0:
        return n
    else:
        if memo[(n, m)] != float("inf"):
            return memo[(n, m)]

        memo[(n, m)] = gcd(m, n % m)
        return memo[(n, m)]


a, b, c = LI()

n = gcd(a, gcd(b, c))
ans = 0
for i in [a, b, c]:
    ans += i // n - 1

print(ans)
