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
A = [list(S().split()) for _ in range(H)]
pos = defaultdict(list)
tp = set()

for i in range(H):
    for j in range(W):
        pos[A[i][j]].append((i, j))
        tp.add(A[i][j])


N = I()
pv = dict()
vp = dict()
for t in tp:
    pv[t] = set()
    vp[t] = set()

for _ in range(N):
    p, v = S().split()
    pv[p].add(v)
    vp[v].add(p)

q = queue.Queue()
visit = [False] * (H * W)

dir = [[1, 1], [1, 0], [1, -1], [0, 1], [0, -1], [-1, 1], [-1, 0], [-1, -1]]

rem = []
for k, v in vp.items():
    if len(v) == 0:
        q.put(k)
        rem.append(k)
for r in rem:
    vp.pop(r)

while not q.empty():
    an = q.get()
    for pi, pj in pos[an]:
        if A[pi][pj] != an:
            continue
        for di, dj in dir:
            if 0 <= pi + di < H and 0 <= pj + dj < W and A[pi + di][pj + dj] in pv[an]:
                A[pi + di][pj + dj] = "-"

    for v in pv[an]:
        vp[v].remove(an)

    rem = []
    for k, v in vp.items():
        if len(v) == 0:
            q.put(k)
            rem.append(k)
    for r in rem:
        vp.pop(r)

for a in A:
    print(*a)

"""
その動物が捕食する動物を管理するpv
その動物が捕食される動物を管理するvp
の2つを見て、vpのvalueが空ならば、もう捕食されない動物のため、捕食をする。
捕食をするのはpvを見て行い、捕食が終わったらpvの内容からvpの要素数を減らす。
"""
