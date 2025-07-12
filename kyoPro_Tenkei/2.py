# fmt: off
from collections import *
from itertools import *
import bisect, copy, heapq, math, numpy, string, queue
from sortedcontainers import *
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


def judge(s):
    stack = []
    for si in s:
        if si == "(":
            stack.append(si)
        else:
            if len(stack) == 0:
                return False
            stack.pop()

    return len(stack) == 0


n = I()
ans = []
for i in range(2**n):
    b = bin(i)[2:].zfill(n)
    s = b.replace("0", "(").replace("1", ")")

    if judge(s):
        ans.append(s)

print("\n".join(sorted(ans)))
