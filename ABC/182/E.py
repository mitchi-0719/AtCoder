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

h, w, n, m = map(int, input().split())
s1 = [[0 for _ in range(w)] for __ in range(h)]
s2 = [[0 for _ in range(w)] for __ in range(h)]

l = [LI() for _ in range(n)]
for _ in range(m):
    c, d = LI()
    c -= 1
    d -= 1

    s1[c][d] = -1
    s2[c][d] = -1

for a, b in l:
    a -= 1
    b -= 1
    if s1[a][b] != 1:
        i = a
        while True:
            if i == -1 or s1[i][b] == -1:
                break
            s1[i][b] = 1
            i -= 1
        i = a
        while True:
            if i == h or s1[i][b] == -1:
                break
            s1[i][b] = 1
            i += 1

    if s2[a][b] != 1:
        i = b
        while True:
            if i == -1 or s2[a][i] == -1:
                break
            s2[a][i] = 1
            i -= 1
        i = b
        while True:
            if i == w or s2[a][i] == -1:
                break
            s2[a][i] = 1
            i += 1

ans = 0
for i in range(h):
    for j in range(w):
        if s1[i][j] == 1 or s2[i][j] == 1:
            ans += 1

print(ans)
