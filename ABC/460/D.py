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
def yes_no(b): return yes if b else no
def sigma(n): (n * (n + 1)) // 2


dir8 = [(-1,-1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]
dir4 = [(0, -1), (1, 0),(0, 1), (-1, 0)]
# fmt: on

H, W = LI()
S = [SI() for _ in range(H)]
d = [[inf] * W for _ in range(H)]
b = [["." for _ in range(W)] for _ in range(H)]

q = deque()

for i in range(H):
    for j in range(W):
        if S[i][j] == "#":
            for di, dj in dir8:
                if 0 <= i + di < H and 0 <= j + dj < W and S[i + di][j + dj] == ".":
                    b[i + di][j + dj] = "#"

for i in range(H):
    for j in range(W):
        if b[i][j] == "#":
            q.append((i, j))
            d[i][j] = 0

while len(q) != 0:
    i, j = q.popleft()
    for di, dj in dir8:
        if 0 <= i + di < H and 0 <= j + dj < W and d[i + di][j + dj] == inf:
            d[i + di][j + dj] = d[i][j] + 1
            q.append((i + di, j + dj))

for i in range(H):
    for j in range(W):
        if d[i][j] % 2 == 1:
            print("#", end="")
        else:
            print(".", end="")

    print()
