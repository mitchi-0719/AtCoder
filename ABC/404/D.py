# fmt: off
from collections import *
from itertools import *
import bisect, copy, heapq, math, numpy, string
import sys

def I(): return int(sys.stdin.readline().rstrip()) # 数値
def LI(): return list(map(int, sys.stdin.readline().rstrip().split())) # 数値リスト
def S(): return sys.stdin.readline().rstrip() # 文字列
def LS(): return list(sys.stdin.readline().rstrip().split()) # 文字列リスト
def yes_no(b): return "Yes" if b else "No"

sys.setrecursionlimit(10**8)
mod = 998244353
# fmt: on


def base_n(num_10, n):
    str_n = ""
    while num_10:
        if num_10 % n >= 10:
            return -1
        str_n += str(num_10 % n)
        num_10 //= n
    return str_n


n, m = LI()
c = LI()
k = []
a = []

b = [[] for _ in range(n)]
for i in range(m):
    [ki, *ai] = LI()
    k.append(ki)
    a.append([aii - 1 for aii in ai])

    for aii in ai:
        b[aii - 1].append(i)

costs = [float("inf") for _ in range(3**n)]

for i in range(3**n):
    th_num = base_n(i, 3)
    cost = 0
    cnt = [0 for _ in range(m)]
    for j in range(len(th_num)):
        num = int(th_num[j])

        for bi in b[j]:
            cnt[bi] += 1 * num

        cost += num * c[j]

    if all([v >= 2 for v in cnt]):
        costs[i] = cost

print(min(costs))
