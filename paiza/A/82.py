# fmt: off
from collections import *
from itertools import *
import bisect, copy, heapq, math, numpy, string, queue
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
# fmt: on


H, W = LI()
s = [list(S()) for _ in range(H)]


def id(i, j):
    return j + W * i


def bfs(g, start, stop):
    vis = set()
    q = queue.Queue()
    vis.add(start)
    q.put(start)

    while not q.empty():
        pos = q.get()
        for nex in g[pos]:
            if nex == stop:
                continue
            if nex not in vis:
                vis.add(nex)
                q.put(nex)

    return len(vis)


def solve(i, j):
    for di, dj in dir:
        if 0 <= i + di < H and 0 <= j + dj < W and s[i + di][j + dj] == "#":
            if bfs(g, id(i + di, j + dj), id(i, j)) != c - 1:
                return False

    return True


g = [[] for _ in range(H * W)]

ans = 0
dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
for i in range(H):
    for j in range(W):
        if s[i][j] == ".":
            ans += 1
        else:
            for di, dj in dir:
                if 0 <= i + di < H and 0 <= j + dj < W and s[i + di][j + dj] == "#":
                    g[id(i, j)].append(id(i + di, j + dj))

c = H * W - ans
for i in range(H):
    for j in range(W):
        if s[i][j] == "#":
            ans += 1 if solve(i, j) else 0

print(ans)
