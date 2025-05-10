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


h, w = LI()
s = [(S()) for _ in range(h)]

ans = [[None for _ in range(w)] for _ in range(h)]
q = queue.Queue()

for y in range(h):
    for x in range(w):
        if s[y][x] == "E":
            q.put((x, y))
            ans[y][x] = [0, -1]
        else:
            ans[y][x] = [float("inf"), -1]


dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
dir_s = ["^", "v", "<", ">"]


# 幅優先探索
while not q.empty():
    x, y = q.get()
    d = ans[y][x][0]
    for i in range(4):
        dx, dy = dir[i]
        if (
            0 <= x + dx < w
            and 0 <= y + dy < h
            and s[y + dy][x + dx] == "."
            and ans[y + dy][x + dx][0] == float("inf")
        ):
            ans[y + dy][x + dx] = [d + 1, i]
            q.put((x + dx, y + dy))


for y in range(h):
    for x in range(w):
        dist, dir_i = ans[y][x]
        if dist == 0:
            print("E", end="")
        elif dist == float("inf"):
            print("#", end="")
        else:
            print(dir_s[dir_i], end="")

    print()
