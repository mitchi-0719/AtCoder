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

az = [chr(ord("a") + i) for i in range(26)]


def solve():
    n = I()
    s = S()

    st = -1
    for i in range(n - 1):
        if s[i] > s[i + 1]:
            st = i
            break

    if st == -1:
        print(s)
        return

    ed = -1

    for i in range(n):
        if i == st:
            ed = i
        elif i < st:
            print(s[i], end="")
        else:
            if s[ed] >= s[i] or ed == -1:
                print(s[i], end="")
            else:
                print(s[ed] + s[i], end="")
                ed = -1
    if ed != -1:
        print(s[ed], end="")

    print()


t = I()
for _ in range(t):
    solve()
