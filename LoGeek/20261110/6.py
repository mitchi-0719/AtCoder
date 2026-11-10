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

H, W, K = LI()
S = [list(SI()) for _ in range(H)]

r = [0] * H
c = [0] * W
v = [[False] * W for _ in range(H)]

for i in range(H):
    for j in range(W):
        if S[i][j] == "#":
            r[i] += 1
            c[j] += 1

q = deque()
for i in range(H):
    for j in range(W):
        if r[i] == c[j] == 0:
            q.append((i, j, 0))
            v[i][j] = True


def n(i, j):
    result = []
    for di, dj in dir4:
        if (
            0 <= i + di < H
            and 0 <= j + dj < W
            and S[i + di][j + dj] == "."
            and not v[i + di][j + dj]
        ):
            result.append((i + di, j + dj))

    return result


ans = len(q)
while len(q) != 0:
    i, j, k = q.popleft()
    for ni, nj in n(i, j):
        if not v[ni][nj]:
            v[ni][nj] = True
            if k < K:
                ans += 1
            else:
                break
            q.append((ni, nj, k + 1))

print(ans)
