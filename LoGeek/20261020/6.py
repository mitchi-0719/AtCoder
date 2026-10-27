# fmt: off
from collections import *
from itertools import *
import bisect, copy, heapq, math, numpy, string, queue
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


def get_prime(n):
    sieve = [True] * (n + 1)
    i = 2
    while i * i <= n:
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
        i += 1
    return [i for i in range(2, n + 1) if sieve[i]]


S = SI()
n = len(S)
p = get_prime(10**7)

for pi in p:
    d = dict()
    use = set()
    sp = str(pi)
    if n != len(sp):
        continue

    for i in range(n):
        if d.get(S[i]) == None or sp[i] not in use:
            d[S[i]] = sp[i]
            use = sp[i]
        elif d[S[i]] != sp[i]:
            break
        print(d)
    else:
        print(pi)
        exit()

print(-1)
