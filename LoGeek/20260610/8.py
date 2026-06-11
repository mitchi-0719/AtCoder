# fmt: off
from collections import *
from itertools import *
import bisect, copy, heapq, math, numpy, string, queue
from sortedcontainers import *
from functools import lru_cache
import sys
from pprint import pprint

sys.setrecursionlimit(10**8)
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

N = I()
S = [SI() for _ in range(N)]
idx = [i for i in range(N)]

S, idx = zip(*sorted(zip(S, idx)))

ans = [0] * N


def p(s1, s2):
    n, m = len(s1), len(s2)
    c = 0
    while c < n and c < m and s1[c] == s2[c]:
        c += 1

    return c


for i in range(N):
    if i == 0:
        s1 = S[i]
        s2 = S[i + 1]
        ii = idx[i]
        ans[ii] = p(s1, s2)
    elif i == N - 1:
        s1 = S[i]
        s2 = S[i - 1]
        ii = idx[i]
        ans[ii] = p(s1, s2)
    else:
        s1 = S[i]
        s2 = S[i + 1]
        s3 = S[i - 1]
        ii = idx[i]
        ans[ii] = max(p(s1, s2), p(s1, s3))


for a in ans:
    print(a)

"""
解説AC

文字列の前側の一致数は辞書順にソートして、その前後を確認すれば良い。
"""
