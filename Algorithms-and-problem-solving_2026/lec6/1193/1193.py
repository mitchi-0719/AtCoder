# fmt: off
from collections import *
from itertools import *
import bisect, copy, heapq, math, string, queue
from functools import lru_cache
import sys
from pprint import pprint

sys.setrecursionlimit(10**8)
yes = "Yes"
no = "No"
mod = 998244353
inf = float("inf")

def I(): return int(sys.stdin.readline().rstrip()) # 数値
def LI(): return list(map(int, sys.stdin.readline().rstrip().split())) # 数値リスト
def S(): return sys.stdin.readline().rstrip() # 文字列
def LS(): return list(sys.stdin.readline().rstrip().split()) # 文字列リスト
def yes_no(b): return yes if b else no
def sigma(n): (n * (n + 1)) // 2


dir8 = [(-1,-1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]
dir4 = [(0, -1), (1, 0),(0, 1), (-1, 0)]
# fmt: on


def solve():
    H = I()

    if H == 0:  # 終了条件
        return 1

    S = [LI() for _ in range(H)]
    score = 0

    changed = True
    while changed:
        st = -1
        ed = -1
        changed = False
        for i in range(H):
            prev = -1
            cnt = 1
            for j in range(5):
                if i < 0:
                    continue
                if prev == S[i][j]:
                    cnt += 1
                else:
                    if cnt >= 3 and prev != 0:
                        ed = j - 1
                        st = ed - cnt + 1
                        break
                    elif cnt <= 2:
                        cnt = 1
                        prev = S[i][j]

            if cnt >= 3 and prev != 0:
                if st == -1 or ed == -1:
                    ed = j
                    st = ed - cnt + 1
                changed = True
                print(i, list(range(st, ed + 1)))
                for k in range(st, ed + 1):
                    score += S[i][k]
                    S[i][k] = 0

        t = [[0] * 5 for _ in range(H)]
        for j in range(5):
            k = H - 1
            for i in range(H)[::-1]:
                if S[i][j] > 0:
                    t[k][j] = S[i][j]
                    k -= 1

        S = t
        pprint(S)
        print()

    print(score)


while not solve():
    ...
