# fmt: off
from collections import *
from itertools import *
import bisect, copy, heapq, math,  string, queue
from sortedcontainers import *
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

N, K = LI()
A = LI()

ans = 0
x = math.comb(N - 1, K - 1)
ans = x * sum(a**2 for a in A) % mod
# for a in A:
#     ans += (a**2 % mod * x) % mod
#     ans %= mod

# ans = x * sum([pow(a, 2, mod) for a in A]) % mod

if N <= 1 or K <= 1:
    print(ans % mod)
    exit()

s = sum(A)
tmp = 0
for i in range(N - 1):
    s -= A[i]
    tmp += (A[i] % mod * s % mod) % mod
    tmp %= mod

y = math.comb(N - 2, K - 2)
ans += ((2 * tmp) % mod * y) % mod

print(ans % mod)
