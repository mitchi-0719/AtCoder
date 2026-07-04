# fmt: off
from collections import *
from itertools import *
import bisect, copy, heapq, math, string, queue
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


def solve():
    N = int(input())
    if N == 0:
        return True

    C, J = [], []
    jem = []
    non_jem = []
    for j in range(N):
        c, j = map(int, input().split())
        C.append(c)
        J.append(j)
        if j > 0:
            jem.append(c)
        else:
            non_jem.append(c)
    jem_i = list(range(len(jem)))
    non_jem_i = list(range(len(non_jem)))

    J_sum = sum(J)
    if J_sum >= N - 1:
        print(min(jem))  # XXX
        return

    if len(jem) == 0:
        print(sum(C))
        return

    jem, jem_i = zip(*sorted(zip(jem, jem_i), reverse=True))
    non_jem, non_jem_i = zip(*sorted(zip(non_jem, non_jem_i)))
    jem = list(jem)
    jem_i = list(jem_i)
    non_jem = list(non_jem)
    non_jem_i = list(non_jem_i)

    print(jem)
    print(non_jem)

    ans = jem.pop()
    mod_j = J_sum - (len(jem) - 1)
    # print(mod_j)
    for i in range(mod_j):
        if non_jem:
            non_jem.pop()

    print(sum(non_jem) + ans)

    while jem and non_jem:
        if jem[-1] < non_jem[-1]:
            # print("pop", jem[-1], non_jem[-1])
            ans += jem.pop()
            non_jem.pop()
        else:
            break

    ans += sum(non_jem)
    # print(jem)
    # print(non_jem)
    # print(ans)


while not solve():
    ...
