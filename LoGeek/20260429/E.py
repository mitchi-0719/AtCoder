# fmt: off
from collections import *
from itertools import *
import bisect, copy, heapq, math, numpy, string, queue
from sortedcontainers import *
from functools import lru_cache
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
yes = "Yes"
no = "No"

dir8 = [(-1,-1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]
dir4 = [(0, -1), (1, 0),(0, 1), (-1, 0)]

# fmt: on

n = I()
a = [list(map(int, list(S()))) for _ in range(n)]
mx = max([max(ai) for ai in a])

mx_i = []
for i in range(n):
    for j in range(n):
        if a[i][j] == mx:
            mx_i.append((i, j))

num = -1
ans = 0


def dfs(i, j, di, dj, k, tmp):
    global ans
    if k == n:
        ans = max(ans, tmp)
        return

    ai = a[(i + di * k) % n][(j + dj * k) % n]
    if tmp * 10 + ai >= ans % (10 ^ k):
        tmp = tmp * 10 + ai
        dfs(i, j, di, dj, k + 1, tmp)


for i, j in mx_i:
    for di, dj in dir8:
        tmp = 0
        dfs(i, j, di, dj, 0, tmp)

print(ans)
