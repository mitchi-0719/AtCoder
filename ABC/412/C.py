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
def print_nobreak(t, end=""): print(t, end=end)

sys.setrecursionlimit(10**8)
mod = 998244353
# fmt: on


def solve():
    n = I()
    s = LI()
    d1 = s[0]
    dn = s[-1]

    cur = d1
    cnt = 2

    while True:
        if cur * 2 >= dn:
            print(cnt)
            return

        mx = 0
        for si in s[1:-1]:
            if cur * 2 >= si and mx > si:
                mx = si

        cnt += 1
        cur = mx

        if mx * 2 >= dn:
            print(cnt)
            return

        if mx == 0:
            print(-1)
            return


t = I()
for _ in range(t):
    solve()
